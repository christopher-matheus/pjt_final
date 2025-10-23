from flask import Blueprint, request, jsonify
from core.materias.materia import Materia
from core.materias.materias_service import MateriaService
from core.autenticação.aut import autenticacao

materia_controller = Blueprint('materia', __name__, url_prefix='/materias')

materias_service = MateriaService()

@materia_controller.route('/', methods=['GET'])
@autenticacao
def listar_materias():
    materias = materias_service.listar_materias()
    return jsonify(materias)

@materia_controller.route('/', methods=['POST'])
@autenticacao
def adicionar_materia():
    dados = request.get_json()
    obj_materia = materia(id=0, nome=dados['nome'], cpf=dados['cpf'], idade=dados['idade'])
    materia = materias_service.adicionar_materia(obj_materia)
    return jsonify(materia), 201

@materia_controller.route('/<int:materia_id>', methods=['GET'])
@autenticacao
def obter_materia(id):
    materia = materias_service.obter_materia_por_id(id)
    if materia:
        return jsonify(materia)
    else:
        return jsonify({"error": "materia não encontrado"}), 404

@materia_controller.route('/<int:materia_id>', methods=['DELETE'])
@autenticacao
def remover_materia(materia_id):
    sucesso = materias_service.remover_materia(materia_id)
    if sucesso:
        return jsonify(sucesso), 200
    else:
        return jsonify({"error": "materia não encontrado"}), 404
    
@materia_controller.route('/', methods=['PUT'])
@autenticacao
def atualizar_materia():
    dados = request.get_json()
    obj_materia = materia(id=dados['id'], nome=dados['nome'], sg_crc=dados['sg_crc'], descricao=dados['descricao'])
    materia = materias_service.atualizar_materia(obj_materia)
    if materia:
        return jsonify(materia)
    else:
        return jsonify({"error": "materia não encontrada"}), 404