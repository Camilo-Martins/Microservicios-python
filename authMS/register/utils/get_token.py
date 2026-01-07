import os
from jose import jwt
from dotenv import load_dotenv

def generateToken(payload):
    token = jwt.encode(payload , os.getenv("SECRET_KEY"), algorithm="HS512")
    return token
