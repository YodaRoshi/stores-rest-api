from hmac import compare_digest
from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    # user = username_table.get(username, None)
    if user and compare_digest(user.password, password):
        return user

# payload has JWT
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
    # return userid_table.get(user_id, None)
