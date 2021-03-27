import sqlite3
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


if __name__ == '__main__':

    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
