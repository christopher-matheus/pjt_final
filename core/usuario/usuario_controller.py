from flask import Blueprint, request, jsonify
from core.usuario.usuario import Usuario
from core.usuario.usuario_service import UsuarioService

usuario_controller = Blueprint('usuario', __name__, url_prefix='/usuarios')

usuarios_service = UsuarioService()

@usuario_controller.route('/', methods=['GET'])
def listar_usuarios():
    usuarios = usuarios_service.listar_usuarios()
    return jsonify(usuarios)

@usuario_controller.route('/', methods=['POST'])
def adicionar_usuario():
    dados = request.get_json()
    obj_usuario = usuario(id=0, nome=dados['nome'], cpf=dados['cpf'], idade=dados['idade'])
    usuario = usuarios_service.adicionar_usuario(obj_usuario)
    return jsonify(usuario), 201

@usuario_controller.route('/<int:usuario_id>', methods=['GET'])
def obter_usuario(id):
    usuario = usuarios_service.obter_usuario_por_id(id)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({"error": "usuario não encontrado"}), 404

@usuario_controller.route('/<int:usuario_id>', methods=['DELETE'])
def remover_usuario(usuario_id):
    sucesso = usuarios_service.remover_usuario(usuario_id)
    if sucesso:
        return jsonify(sucesso), 200
    else:
        return jsonify({"error": "usuario não encontrado"}), 404
    
@usuario_controller.route('/', methods=['PUT'])
def atualizar_usuario():
    dados = request.get_json()
    obj_usuario = usuario(id=dados['id'], nome=dados['nome'], rm=dados['rm'], cpf=dados['cpf'], idade=dados['idade'])
    usuario = usuarios_service.atualizar_usuario(obj_usuario)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({"error": "usuario não encontrado"}), 404