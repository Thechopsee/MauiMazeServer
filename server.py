from flask import Flask, request, jsonify
import sqlite3 
import datetime
import json
from repositories.mazeRepository import MazeRepository
from repositories.userRepository import UserRepository
from repositories.VCRepository import VCRepository
from repositories.recordsRepository import RecordRepository
from tools.VerificationCodeGenerator import VerificationCodeGenerator
import os

app = Flask(__name__)

@app.route('/saveMaze', methods=['POST'])
def saveMaze():
    data = request.get_json()
    id = data.get('userID')
    edges = data.get('edges')
    mazeid=MazeRepository.saveMazetoDatabase(id,"Classic")
    print(edges[0]['Cell1'])
    upredges=[]
    for edge in edges:
        tupled=(mazeid,edge['Cell1'],edge['Cell2'])
        upredges.append((tupled))
    print(upredges)
    MazeRepository.saveEdgeToDatabase(upredges)
    response = {'message': id}
    status_code = 200
    return jsonify(response), status_code
@app.route('/loadMaze', methods=['POST'])
def loadMaze():
    data = request.get_json()
    id = data.get('mazeID')
    result=MazeRepository.getMaze(id)
    response =  {'message': result}
    status_code = 200
    return jsonify(response), status_code
@app.route('/loadMazeCount', methods=['POST'])
def loadMazeCount():
    data = request.get_json()
    id = data.get('userID')
    result=MazeRepository.getMazeCount(id)
    response =  {'message': result}
    status_code = 200
    return jsonify(response), status_code

@app.route('/loadMazeList', methods=['POST'])
def loadMazeList():
    data = request.get_json()
    id = data.get('userID')
    res=MazeRepository.getMazeList(id)
    response =  {'descriptions': res}
    status_code = 200
    return jsonify(response), status_code

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    print(email)
    print(password)
    id=UserRepository.trytoLoginDatabase(email,password)[0]

    if id>0:
        response = {'message': id}
        status_code = 200
    else:
        response = {'message': -1}
        status_code = 401

    return jsonify(response), status_code
    
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    code = data.get('code')
    result=VCRepository.isCodeTaken(code)
    print(result)
    if(result==0):
        UserRepository.registerUser(email,password)
        VCRepository.updateCode(code)
        return "ok",200
    elif(result==1):
        return "taken code",401
    else:
        return "server error",500
    

@app.route('/createCode', methods=['GET'])
def createCode():
    kod=VerificationCodeGenerator.generate_verification_code()
    VCRepository.save_verification_code(kod)
    return "ok",200

@app.route('/saveRecord', methods=['POST'])
def saveRecord():
    record = request.get_json()
    grID=RecordRepository.saveRecordtoDatabase(record)
    formatedRecords=[]
    python_object = json.loads(record)
    for move in python_object["records"]:
        tupled=(move["percentagex"],move["percentagey"],move["hitWall"],move["deltaTinMilisec"],grID)
        formatedRecords.append((tupled))
    RecordRepository.saveMovesToDatabase(formatedRecords)

if __name__ == '__main__':
    ip = os.environ.get('IP')
    sport = os.environ.get('port')
    app.run(host=ip, port=sport)
