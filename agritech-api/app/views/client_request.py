from app import app
from flask import jsonify, request, abort
from app.models.client_model import ClientModel 
from app.decorators import token_required

@app.route('/api/v1/clientRequest', methods=['POST'])
@token_required
def add_client_request(current_user):
    """
    This endpoint adds a client request 
    :return: 
    """
    if (not request.json or not 'produce_name'in request.json
                         or not 'quantity'in request.json
                         or not 'price_range' in request.json
                         ):
        abort(400)
    data = request.get_json() or {}
    create_client_request = ClientModel(current_user, data['produce_name'], data['quantity'], data['price_range'])
    return_create_client_request  = create_client_request.create_client_request()
    return jsonify({"message":return_create_client_request}), 201

@app.route('/api/v1/clientRequest', methods = ['GET'])
def get_client_request():
    """
    This endpoint gets all clients requests 
    :return: 
    """
    client_requests_list = ClientModel.get_client_requsts()
    return jsonify({'Client Request': client_requests_list}),200