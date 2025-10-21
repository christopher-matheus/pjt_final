from flask import Blueprint, request, jsonify
from core.professor.professor_service import ProfessorService
from core.professor.professor import Professor
from core.autenticação.aut import autenticacao

service = ProfessorService()

controller = Blueprint('professor', __name__, url_prefix='/professors')

@controller.route('/', methods=['GET'])
@autenticacao
def listar():
    objeto = service.listar_professors()
    return jsonify(objeto)

@controller.route('/', methods=['POST'])
@autenticacao
def adicionar():
    dados = request.get_json()
    obj = Professor(id=0, nome=dados["nome"], 
                      id=dados["id"], 
                      formacao=dados["formacao"])
    objeto = service.adicionar_professor(obj)
    return jsonify(objeto), 201

@controller.route('/<int:id>', methods=['GET'])
@autenticacao
def obter(id):
    objeto = service.obter_professor_por_id(id)
    if objeto:
        return jsonify(objeto)
    else:
        return jsonify({"erro": "professor não encontrado"}), 404

@controller.route('/<int:id>', methods=['DELETE']) 
@autenticacao   
def remover(id):
    sucesso = service.remover_professor(id)
    return jsonify(sucesso)

@controller.route('/', methods=['PUT'])
@autenticacao
def atualizar():
    dados = request.get_json()
    obj = Professor(id=dados["id"], professor=dados["professor"],
                      id=dados["id"], formacao=dados["formacao"])
    objeto = service.atualizar_professor(obj)
    if objeto:
        return jsonify(objeto)
    else:
        return jsonify({"erro": "professor não encontrado"}), 404