from flask import Flask, request, jsonify, Response
from database import *
app = Flask(__name__)


@app.route('/user.auth', methods=['GET'])
def auth():
    email = request.args.get('email')
    pwd = request.args.get('pwd')
    user = db_helper.user_by_email(email)
    response = {}
    code = 0
    if user == None:
        response["msg"] = "No such user"
        code = 404
    else:
        if user.pwd == pwd:
            response["msg"] = "Wrong password"
            code = 401
        else:
            response["result"] = user.json()
            code = 200
    return jsonify(response), code


@app.route('/user.register', methods=['POST', 'GET'])
def register():
    email = request.args.get('email')

    user = db_helper.user_by_email(email)

    response = {}
    code = 0
    if user != None:
        response['msg'] = "User already exists"
        code = 403
    else:
        pwd = request.args.get('pwd')
        if len(pwd) < 8:
            response['msg'] = "Password must be at least 8 symbols"
            code = 403
        else:
            name = request.args.get('name')
            surname = request.args.get('surname')
            age = request.args.get('age')
            user = db_helper.insert_user(email, pwd, name, surname, age)
            if user != None:
                response['result'] = user.json()
                code = 200
            else:
                response['msg'] = "Internall Error"
                code = 503
    return jsonify(response), code


    



if __name__ == '__main__':

    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
