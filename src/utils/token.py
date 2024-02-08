from datetime import datetime, timedelta, timezone
import jwt

# NOTE: this key is just for testing in dev environment,
# key should be stored in a separated env file
jwt_secret_key = '94sO7Q9iQP8IMTTI6wQhfA7SUlpBRY6r5KZjAb_KbxI'

def generate_jwt_token(user_id: int) -> str:
    payload = {
        "user_id": user_id,
        "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=10)
    }
    token = jwt.encode(payload, jwt_secret_key, algorithm='HS256')
    return token

    