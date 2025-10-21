from flask import Blueprint, request, jsonify
from core.usuario.usuario_service import UsuarioService
from core.usuario.usuario import Usuario
from core.autenticação.aut import autenticacao

service = UsuarioService()

controller = Blueprint('usuario', __name__, url_prefix='/usuarios')

@controller.route('/', methods=['GET'])
@autenticacao
def listar():
    objeto = service.listar_usuarios()
    return jsonify(objeto)

@controller.route('/', methods=['POST'])
@autenticacao
def adicionar():
    dados = request.get_json()
    obj = Usuario(id=0, usuario=dados["usuario"], 
                      senha=dados["senha"], 
                      ativo=dados["ativo"])
    objeto = service.adicionar_usuario(obj)
    return jsonify(objeto), 201

@controller.route('/<int:id>', methods=['GET'])
@autenticacao
def obter(id):
    objeto = service.obter_usuario_por_id(id)
    if objeto:
        return jsonify(objeto)
    else:
        return jsonify({"erro": "Usuario não encontrado"}), 404

@controller.route('/<int:id>', methods=['DELETE']) 
@autenticacao   
def remover(id):
    sucesso = service.remover_usuario(id)
    return jsonify(sucesso)

@controller.route('/', methods=['PUT'])
@autenticacao
def atualizar():
    dados = request.get_json()
    obj = Usuario(id=dados["id"], usuario=dados["usuario"],
                      senha=dados["senha"], ativo=dados["ativo"])
    objeto = service.atualizar_usuario(obj)
    if objeto:
        return jsonify(objeto)
    else:
        return jsonify({"erro": "Usuario não encontrado"}), 404