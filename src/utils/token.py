from datetime import datetime, timedelta, timezone
import jwt

# NOTE: this key is just for testing in dev environment,
# key should be stored in a separated env file
JWT_SECRET_KEY = '94sO7Q9iQP8IMTTI6wQhfA7SUlpBRY6r5KZjAb_KbxI'
ALGORITHM = 'HS256'
EXPIRATION_TIME = 30 # 30 minutes

def generate_jwt_token(data: dict) -> str:
    data_to_encode = data.copy()
    data_to_encode.update({"exp": datetime.utcnow() + timedelta(minutes=30)})
    token = jwt.encode(data_to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_jwt_token(encoded_token: str) -> str:
    decoded_data = jwt.decode(encoded_token, JWT_SECRET_KEY, algorithms=["HS256"])
    return decoded_data["sub"] # returns email encoded on payload


    