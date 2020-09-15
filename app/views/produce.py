from app import app
from flask import jsonify, request, abort
from app.models.produce_model import ProduceModel
from app.decorators import token_required

@app.route('/api/v1/produce', methods=['POST'])
@token_required
def add_farmer_produce(current_user):
    """
    This endpoint adds a produce 
    :return: 
    """
    if (not request.json or not 'produce_name'in request.json
                         or not 'quantity'in request.json
                         or not 'unit_price' in request.json
                         ):
        abort(400)
    data = request.get_json() or {}
    create_farmer_produce =ProduceModel(current_user, data['produce_name'], data['quantity'], data['unit_price'])
    return_create_farmer_produce  = create_farmer_produce.create_produce()
    return jsonify({"message":return_create_farmer_produce}), 201

@app.route('/api/v1/farmerProduce', methods = ['GET'])
def get_products():
    """
    This endpoint gets all farmer produce 
    :return: 
    """
    farmer_produce_list = ProduceModel.get_farmer_produce()
    return jsonify({'Farmer Produce': farmer_produce_list}),200