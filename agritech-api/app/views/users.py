from app import app
from app.models.user_model import UserModel
from flask import jsonify, request,make_response, abort
from app.decorators import generate_token, token_required
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def index():
  """
  index route
  return
  """
  return "<h2>Welcome to Agribid</h2>"

@app.route('/api/v1/auth/signup', methods = ['POST'])
def create_user():
    if (not request.json or not 'name'in request.json
                         or not 'email' in request.json
                         or not 'password' in request.json
                         or not 'confirm_password' in request.json
                         or not 'role' in request.json
                         ):
        return jsonify({'message':'All fields are required'}), 400

    data = request.get_json() or {}
    if data['password'] != data['confirm_password']:
        return jsonify({'message':'Passwords do not match'}), 422
    password =generate_password_hash(data['password'])
    register_user = UserModel.register_user(data['name'], data['email'], password, data['role'])
    if register_user == "Email already exists":
            return jsonify({"message":register_user}), 403
    return jsonify({"message":register_user}), 201

@app.route('/api/v1/users', methods = ['GET'])
def get_users():
    users_list = UserModel.get_users()
    if users_list == "No Users":
        return jsonify({'users': users_list}), 404
    return jsonify({'users': users_list}), 200

@app.route('/api/v1/auth/login',methods=['POST'])
def login():
    if (not request.json or not 'email' in request.json
                         or not 'password' in request.json):
        return jsonify({"message":"wrong params"})
    data = request.get_json() or {}

    if user == "user not found":
        return jsonify({'message':'Invalid username and password'}), 401

    if not check_password_hash(user[3], data['password']):
        return jsonify({"message":"Wrong password"}), 404

    return jsonify({
                'id':user[0],
                'name':user[1],
                'role':user[4],
                'email':user[2],
                'loginstatus': "Login successful",
                'x-access-token':generate_token(user[0])
                }),200