
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="Username is required"
        )
    parser.add_argument('password',
        type=str,
        required=True,
        help="password is required"
        )
    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A User with that username already exists"}, 400

        user = UserModel(**data) # unpack a dictionary because property in both data and user have the same property
        user.save_to_db()

        return {"message": "user created successfully"}, 201
