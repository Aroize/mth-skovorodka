from flask import Flask, request, jsonify, Response
from database import *
import time
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
    if user is not None:
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
            if user is not None:
                response['result'] = user.json()
                code = 200
            else:
                response['msg'] = "Internall Error"
                code = 503
    return jsonify(response), code


@app.route('/stat.click', methods=['POST', 'GET'])
def paperClicked():
    uid = request.args.get('uid')
    p_id = request.args.get('p_id')
    ts = int(time.time() * 1_000)
    event_type = "click"
    result = db_helper.register_stat(uid, p_id, ts, event_type)
    response = {}
    code = 0
    if result:
        response["response"] = 0
        code = 200
    else:
        response["msg"] = "Internall Error"
        code = 500
    return jsonify(response), code


@app.route('/stat.close', methods=['POST', 'GET'])
def paperLeft():
    uid = request.args.get('uid')
    p_id = request.args.get('p_id')
    ts = int(time.time() * 1_000)
    event_type = "close"
    result = db_helper.register_stat(uid, p_id, ts, event_type)
    response = {}
    code = 0
    if result:
        response["response"] = 0
        code = 200
    else:
        response["msg"] = "Internall Error"
        code = 500
    return jsonify(response), code


@app.route('/fave.add', methods=['POST', 'GET'])
def faveAdd():
    uid = request.args.get('uid')
    p_id = request.args.get('p_id')
    result = db_helper.add_to_fave(uid, p_id)
    response = {}
    code = 0
    if result is not None:
        if result:
            code = 200
            response["response"] = 0
        else:
            code = 409
            response["msg"] = "Already in favs"
    else:
        code = 500
        response["msg"] = "Internal Error"
    return jsonify(response), code


@app.route('/fave.remove', methods=['POST', 'GET'])
def faveRemove():
    uid = request.args.get('uid')
    p_id = request.args.get('p_id')
    result = db_helper.remove_from_favs(uid, p_id)
    response = {}
    code = 0
    if result is not None:
        if result:
            code = 200
            response["response"] = 0
        else:
            code = 404
            response["msg"] = "Not in favs"
    else:
        code = 500
        response["msg"] = "Internal Error"
    return jsonify(response), code


@app.route('/user.pickThemes', methods=['POST', 'GET'])
def pickThemes():
    uid = request.args.get('uid')
    themes = request.args.get('themes').split(',')
    result = db_helper.user_pick_themes(uid, themes)
    response = {}
    code = 0
    if result is not None:
        code = 200
        response["response"] = 0
    else:
        code = 500
        response["mgs"] = "Internal Error"
    return jsonify(response), code


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
