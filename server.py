from flask import Flask, request, jsonify
import sqlite3 
import datetime
import sys
import json
from repositories.mazeRepository import MazeRepository
from repositories.userRepository import UserRepository
from repositories.VCRepository import VCRepository
from repositories.recordsRepository import RecordRepository
from tools.VerificationCodeGenerator import VerificationCodeGenerator

from databaseServices.databaseAdapter import DatabaseAdapter
from databaseServices.sqliteAdapter import SqliteAdapter
import os


app = Flask(__name__)

@app.route('/saveMaze', methods=['POST'])
def saveMaze():
    data = request.get_json()
    id = data.get('userID')
    mazedto = data.get('mazedto')
    mazeid=MazeRepository.saveMazetoDatabase(id,"Classic",mazedto["startCell"],mazedto["endCell"],mazedto["size"],database,adapter)
    upredges=[]
    for edge in mazedto['edges']:
        tupled=(mazeid,edge['Cell1'],edge['Cell2'])
        upredges.append((tupled))
    MazeRepository.saveEdgeToDatabase(upredges,database,adapter)
    response = {'message': id}
    status_code = 200
    return jsonify(response), status_code
@app.route('/loadMaze', methods=['POST'])
def loadMaze():
    data = request.get_json()
    id = data.get('mazeID')
    result=MazeRepository.getMaze(id,database,adapter)
    response =  result
    status_code = 200
    return jsonify(response), status_code

@app.route('/loadRecordByMaze', methods=['POST'])
def loadRecord():
    data = request.get_json()
    id = data.get('mazeID')
    result=RecordRepository.loadRecordsbyMaze(id,database,adapter)
    response = json.dumps([record.to_dict() for record in result])
    status_code = 200
    return response, status_code

@app.route('/loadRecordByUser', methods=['POST'])
def loadRecordbyuser():
    data = request.get_json()
    id = data.get('userID')
    result=RecordRepository.loadRecordsbyUser(id,database,adapter)
    response = json.dumps([record.to_dict()for record in result])
    status_code = 200
    return response, status_code

@app.route('/loadMazeCount', methods=['POST'])
def loadMazeCount():
    data = request.get_json()
    id = data.get('userID')
    result=MazeRepository.getMazeCount(id,database,adapter)[0]
    response =  {'message': result}
    status_code = 200
    return jsonify(response), status_code

@app.route('/loadMazeList', methods=['POST'])
def loadMazeList():
    data = request.get_json()
    id = data.get('userID')
    res=MazeRepository.getMazeList(id,database,adapter)
    response =  {'descriptions': res}
    status_code = 200
    return jsonify(response), status_code

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    res=UserRepository.trytoLoginDatabase(email,password,database,adapter)
    if(res['id']==-1):
        response = res
        status_code = 401
    else :
        response=res
        status_code = 200        

    return jsonify(response), status_code
    
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    code = data.get('code')
    result=VCRepository.isCodeTaken(code,database,adapter)
    print(result)
    if(result==0):
        UserRepository.registerUser(email,password,database,adapter)
        VCRepository.updateCode(code)
        return "ok",200
    elif(result==1):
        return "taken code",401
    else:
        return "server error",500
    

@app.route('/createCode', methods=['GET'])
def createCode():
    kod=VerificationCodeGenerator.generate_verification_code()
    VCRepository.save_verification_code(kod,database,adapter)
    return "ok",200

@app.route('/saveRecord', methods=['POST'])
def saveRecord():
    record = request.get_json()
    grID=RecordRepository.saveRecordtoDatabase(record,database,adapter)
    formatedRecords=[]
    for move in record["records"]:
        hw=0
        if(move["hitWall"] == 'True'):
            hw=1
            print(move['cell'])
        tupled=(move["percentagex"],move["percentagey"],hw,move["deltaTinMilisec"],grID,move['cell'])
        formatedRecords.append((tupled))
    RecordRepository.saveMovesToDatabase(formatedRecords,database,adapter)
    return "ok",200

database=os.environ.get('database_connection_string')
adapter : DatabaseAdapter
if __name__ == '__main__':
    ip = os.environ.get('IP')
    sport = os.environ.get('port')
    db_type=os.environ.get('database_type')
    if(db_type == 'SQLITE'):
        adapter=SqliteAdapter()
    app.run(host=ip, port=sport)
