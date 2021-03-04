from ..models import db, UserModel, AdminModel
import json
import jwt
from instance.config import SECRET_KEY
import datetime
from ..util.auth_token import check_auth_token


def register(details):
    # destructuring data
    try:
        firstname = details["firstname"]
        lastname = details["lastname"]
        email = details["email"]
        password = details["password"]
        profilePicture = details["profilePicture"]
        regType = details["regType"]
    except KeyError:
        return json.dumps({"error": True,
                           "message": "One or more fields are missing!"})

    # getting data from model
    if regType == "user":

        # destructuring extra data for user
        try:
            accountType = details["accountType"]
        except KeyError:
            return json.dumps({"error": True,
                               "message": "One or more fields are missing!"})

        status = UserModel.query.filter(UserModel.email == email).first()

    else:

        # destructuring extra data for admin
        try:
            designation = details["designation"]
            lng = details["lng"]
            lat = details["lat"]
        except KeyError:
            return json.dumps({"error": True,
                               "message": "One or more fields are missing!"})

        status = AdminModel.query.filter(AdminModel.email == email).first()

    if status is None:

        if regType == "user":

            data = UserModel(firstname=firstname, lastname=lastname,
                             email=email, password=password,
                             profilePicture=profilePicture,
                             accountType=accountType,
                             dataOfRegister=datetime.datetime.utcnow())

        else:

            data = AdminModel(firstname=firstname, lastname=lastname,
                              email=email, password=password,
                              profilePicture=profilePicture,
                              designation=designation,
                              dataOfRegister=datetime.datetime.utcnow(),
                              lng=lng, lat=lat)

        db.session.add(data)
        db.session.commit()

        return json.dumps({"error": False,
                           "message": "User registered successfully"})

    return {"error": True, "message": "Email already exists"}


def login(details):
    # destructuring data
    try:
        email = details["email"]
        password = details["password"]
        regType = details["regType"]
    except KeyError:
        return json.dumps({"error": True,
                           "message": "One or more fields are missing!"})

    if email == "" or password == "":
        return json.dumps({"error": True, "message": "Empty Fields"})

    if type(email) is not str or type(password) is not str:
        return json.dumps({"error": True, "message": "Wrong data format!"})

    if regType == "user":
        data = UserModel.query.filter(UserModel.email == email).first()
    else:
        data = AdminModel.query.filter(AdminModel.email == email).first()

    if data is not None:
        if data.password == password:
            obj = {
                "email": data.email,
                "created_at": str(datetime.datetime.utcnow()),
                "expire_at": str(datetime.datetime.utcnow()
                                 + datetime.timedelta(days=1))
            }

            if regType == "user":
                # destructuring extra data for user
                try:
                    obj["accountType"] = data.accountType,
                except KeyError:
                    return json.dumps({"error": True,
                                       "message": "One or more fields are missing!"})

            encode_jwt = jwt.encode(obj, SECRET_KEY)

            return json.dumps({"error": False, "token": encode_jwt.decode(),
                               "message": "Logged in successfully!"})

        else:
            return json.dumps({"error": True,
                               "message":
                               "You have entered the wrong password!"})

    return json.dumps({"error": True, "message": "Unknown error!"})
