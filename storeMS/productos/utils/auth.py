import os
from jose import jwt
from dotenv import load_dotenv


def get_admin_id_from_request(request):
    header = request.headers.get('Authorization').split(" ")
    payload = jwt.decode(header[1],  os.getenv("SECRET_KEY"), algorithms=['HS512'])
    return payload["id"]
