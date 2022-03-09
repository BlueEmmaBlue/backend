from flask import Flask, request, jsonify,send_file
import json
import os

app = Flask(__name__)


DIR_PATH = app.root_path


FILE_PATH = f'{DIR_PATH}/list.json'
EXECUTE_PATH = f'{DIR_PATH}/EV_Main.exe'
RESULT_IMG_PATH = f'{DIR_PATH}/result/Probabilisitc EV load profile.png'

@app.route('/getList',methods = ['GET'])
def getConfiguration():
    return jsonify(get_List())
    

@app.route('/updateConfiguration',methods = ['POST'])
def updateConfiguration():
    json_datas = request.get_json()
    config_data = get_config_data()
    if json_datas is not None and len(json_datas) > 0:
        for json_data in json_datas:
            print(json_data)
            config_data['values'][json_data['index']]['Parameters'] = json_data['new_parameter']
        save_config_data(config_data)
    else:
        app.logger.warning("got no param for update configuration")

    
    os.system(EXECUTE_PATH)

    return jsonify({"code":0,"message":"success"})


@app.route('/resultImage',methods = ['GET'])
def resutlImage():
    return send_file(RESULT_IMG_PATH,mimetype='image/png')


def get_List():
    with open(FILE_PATH,'r') as f:
        json_data = json.load(f)
    return json_data

def save_config_data(json_data):
    with open(FILE_PATH,'w') as f:
        json.dump(json_data, f,indent=4)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug = True)
