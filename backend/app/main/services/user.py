from ..models import db, UserModel
import json
import jwt
from instance.config import SECRET_KEY
import datetime
from ..util.auth_token import check_auth_token


def register(details):
    firstname = details["firstname"]
    lastname = details["lastname"]
    email = details["email"]
    password = details["password"]
    profilePicture = details["profilePicture"]
    accountType = details["accountType"]

    status = UserModel.query.filter(UserModel.email == email).first()

    if status is None:

        user = UserModel(firstname=firstname, lastname=lastname,
                         email=email, password=password,
                         profilePicture=profilePicture,
                         accountType=accountType,
                         dataOfRegister=datetime.datetime.utcnow())

        db.session.add(user)
        db.session.commit()

        return json.dumps({"error": False,
                           "message": "User registered successfully"})

    return {"error": True, "message": "Email already exists"}


def login(details):
    try:
        email = details["email"]
        password = details["password"]
    except KeyError:
        return json.dumps({"error": True,
                           "message": "One or more fields are missing!"})

    if email == "" or password == "":
        return json.dumps({"error": True, "message": "Empty Fields"})

    if type(email) is not str or type(password) is not str:
        return json.dumps({"error": True, "message": "Wrong data format!"})

    data = UserModel.query.filter(UserModel.email == email).first()

    if data is not None:
        if data.password == password:
            obj = {
                "email": data.email,
                "accountType": data.accountType,
                "created_at": str(datetime.datetime.utcnow()),
                "expire_at": str(datetime.datetime.utcnow()
                                 + datetime.timedelta(days=1))
            }

            encode_jwt = jwt.encode(obj, SECRET_KEY)

            return json.dumps({"error": False, "token": encode_jwt.decode(),
                               "message": "Logged in successfully!"})

        else:
            return json.dumps({"error": True,
                               "message":
                               "You have entered the wrong password!"})

    return json.dumps({"error": True, "message": "Unknown error!"})
