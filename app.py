from flask import Flask, jsonify
import json
import os

app = Flask(__name__)


DIR_PATH = app.root_path


FILE_PATH = f'{DIR_PATH}/list.json'

@app.route('/getList',methods = ['GET'])
def getConfiguration():
    return jsonify(get_List())


def get_List():
    with open(FILE_PATH,'r') as f:
        json_data = json.load(f)
    return json_data


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug = True)
