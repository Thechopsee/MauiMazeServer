class User:
    ID:int
    email:str
    password:str
    admin:int
    researcher:int
    lastname:str
    firstname:str
    def __init__(self, ID: int, email: str, password: str, admin: int, researcher: int, lastname: str, firstname: str):
        self.ID = ID
        self.email = email
        self.password = password
        self.admin = admin
        self.researcher = researcher
        self.lastname = lastname
        self.firstname = firstname