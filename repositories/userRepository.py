from databaseServices.connectionProvider import ConnectionProvider
from repositories.autorizationTokens import ATRepository

class UserRepository:
    @staticmethod
    def trytoLoginDatabase(email,password):
        sql="SELECT * FROM User WHERE email='"+email+"' and password='"+password+"'"
        adapter=ConnectionProvider().adapter
        res=adapter.getOne(sql)
        code=0
        if(res is  None):
            response = {'id': -1,'role': -1,'email':'-1','firstname':'a','lastname':'a','code':code }
        else:
            role=0
            if(res[3]==1):
                role=2
            elif(res[4]==1):
                role=1
            code=ATRepository.createNewToken(res[0])
            response = {'id': res[0],'role': role,'email':res[1],'firstname':res[5],'lastname':res[6],'code':code}
            
        return response
    @staticmethod        
    def getUsersForResearcher():
        sql="SELECT * FROM User WHERE researcher=0 and admin=0"
        adapter=ConnectionProvider().adapter
        res=adapter.getMany(sql)
        users=[]
        for x in res:
            role=0
            userDTO = {'id': x[0],'role': role,'email':x[1],'firstname':x[5],'lastname':x[6]}
            users.append(userDTO)
        return users
    @staticmethod  
    def getUserRole(id):
        sql="Select admin,researcher from User where ID="+str(id)
        adapter=ConnectionProvider().adapter
        res=adapter.getOne(sql)
        role=1
        if(res[0]==1):
            role+=1
        if(res[1]==1):
            role+=1
        return role
    @staticmethod
    def registerUser(email,password,first,last):
        sql="INSERT INTO User (email,password,firstname,lastname) VALUES (?,?,?,?)"
        adapter=ConnectionProvider().adapter
        return adapter.saveOne(sql,(email,password,first,last))

    @staticmethod
    def deleteUser(email,password):
        sql="DELETE FROM User WHERE email=? AND password=?;"
        adapter=ConnectionProvider().adapter
        adapter.saveOne(sql,(email,password))
