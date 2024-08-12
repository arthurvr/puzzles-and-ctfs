# This code I just copied from the challenge :)

import jwt

SECRET_KEY = "secret"
encoded = jwt.encode({'username': 'arthur', 'admin': True}, SECRET_KEY, algorithm='HS256')
print(encoded)