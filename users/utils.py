
from datetime import datetime, timedelta
from django.conf import settings
import jwt


def jwt_payload_handler(user):
    payload = {
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.utcnow() + timedelta(seconds=settings.JWT_EXPIRATION_DELTA),
        'orig_iat': datetime.utcnow(),
    }

    if hasattr(user, 'email'):
        payload['email'] = user.email

    return payload

def jwt_encode_handler(payload):
    return jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        settings.JWT_ALGORITHM,
    ).decode('utf-8')

