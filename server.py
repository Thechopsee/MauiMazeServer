from flask import Flask, request, jsonify
import json
from repositories.mazeRepository import MazeRepository
from repositories.userRepository import UserRepository
from repositories.VCRepository import VCRepository
from repositories.recordsRepository import RecordRepository
from repositories.autorizationTokens import ATRepository
from tools.VerificationCodeGenerator import VerificationCodeGenerator

from databaseServices.databaseAdapter import DatabaseAdapter
from databaseServices.sqliteAdapter import SqliteAdapter
from databaseServices.connectionProvider import ConnectionProvider
import os


app = Flask(__name__)

@app.route('/mazes', methods=['POST'])
def create_maze():
    data = request.get_json()
    id = data.get('userID')
    mazedto = data.get('mazedto')
    mazeid=MazeRepository.saveMazetoDatabase(id,"Classic",mazedto["startCell"],mazedto["endCell"],mazedto["size"])
    upredges=[]
    for edge in mazedto['edges']:
        tupled=(mazeid,edge['Cell1'],edge['Cell2'])
        upredges.append((tupled))
    MazeRepository.saveEdgeToDatabase(upredges)
    response = {'message': id}
    status_code = 200
    return jsonify(response), status_code
@app.route('/mazes/<maze_id>', methods=['POST'])
def get_maze(maze_id):    
    result=MazeRepository.getMaze(maze_id)
    response =  result
    status_code = 200
    return jsonify(response), status_code

@app.route('/mazes/<maze_id>/records', methods=['POST'])
def get_records_by_maze(maze_id):
    result=RecordRepository.loadRecordsbyMaze(maze_id)
    response = json.dumps([record.to_dict() for record in result])
    status_code = 200
    return response, status_code

@app.route('/users/<user_id>/records', methods=['POST'])
def loadRecordbyuser(user_id):
    result=RecordRepository.loadRecordsbyUser(user_id)
    response = json.dumps([record.to_dict()for record in result])
    status_code = 200
    return response, status_code

@app.route('/users/<user_id>/mcount', methods=['POST'])
def get_maze_count(user_id):
    result=MazeRepository.getMazeCount(user_id)[0]
    response =  {'message': result}
    status_code = 200
    return jsonify(response), status_code

@app.route('/users/<user_id>/mazes', methods=['POST'])
def get_maze_list(user_id):
    res=MazeRepository.getMazeList(user_id)
    response =  {'descriptions': res}
    status_code = 200
    return jsonify(response), status_code

@app.route('/users', methods=['POST'])
def get_users_list():
    data = request.get_json()
    at = data.get('AT')
    res=ATRepository.checkToken(2);
    if(!res):
        return "unauthorized",401
    else:
        users=UserRepository.getUsersForResearcher()
        return jsonify(users), 200
    
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    res=UserRepository.trytoLoginDatabase(email,password)
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
    

@app.route('/codes', methods=['GET'])
def create_codes():
    kod=VerificationCodeGenerator.generate_verification_code()
    VCRepository.save_verification_code(kod)
    return "ok",200

@app.route('/records', methods=['POST'])
def create_record():
    record = request.get_json()
    grID=RecordRepository.saveRecordtoDatabase(record)
    formatedRecords=[]
    for move in record["records"]:
        tupled=(move["percentagex"],move["percentagey"],move["hitWall"],move["deltaTinMilisec"],grID,move['cell'])
        formatedRecords.append((tupled))
    RecordRepository.saveMovesToDatabase(formatedRecords)
    return "ok",200




if __name__ == '__main__':
    ip = os.environ.get('IP')
    sport = os.environ.get('port')
    app.run(host=ip, port=sport)
