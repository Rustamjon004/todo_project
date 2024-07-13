import bcrypt
class Response:
    def __init__(self, data: str, status_code: int):
        self.data = data
        self.status_code = status_code


def hash_password(self,raw_password:str):
    raw_password = raw_password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed.password = bcrypt.hashpw(raw_password,salt)
    return hash_password


def match_password (self,raw_password:str)->bool:
    raw_password == raw_password.encode('utf-8') 
    print (True)
    return bcrypt.checkpw(raw_password,self.password)

def register(self,username,password):
    check_user_query =''' select from users where username =%s ;'''
    cursor.exscute(check_user_query,(username))

    