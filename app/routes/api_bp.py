from flask import Blueprint, jsonify

from app.models import Categoria, Produto, Usuario


api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.route("/produtos", methods=["GET"])
def get_produtos():
    produtos = Produto.query.all()
    
    lista_json = [produto.to_dict() for produto in produtos]
    
    return jsonify(lista_json), 200

@api_bp.route("/categoria", methods=["GET"])
def get_categoria():
    categorias = Categoria.query.all()
    lista_json = [categoria.to_dict() for categoria in categorias]
    
    return jsonify(lista_json), 200
    
    
@api_bp.route("/usuarios", methods=["GET"])
def get_usuarios():
    usuarios = Usuario.query.all()
    lista_json = [usuario.to_dict() for usuario in usuarios]
    
    return jsonify(lista_json), 200