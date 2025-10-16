from flask import Blueprint, request, jsonify
from core.aluno.aluno import Aluno
from core.aluno.aluno_service import AlunoService

aluno_controller = Blueprint('aluno', __name__, url_prefix='/alunos')

alunos_service = AlunoService()

@aluno_controller.route('/', methods=['GET'])
def listar_alunos():
    alunos = alunos_service.listar_alunos()
    return jsonify(alunos)

@aluno_controller.route('/', methods=['POST'])
def adicionar_aluno():
    dados = request.get_json()
    obj_aluno = Aluno(id=0, nome=dados['nome'], rm=dados['rm'], cpf=dados['cpf'], idade=dados['idade'])
    aluno = alunos_service.adicionar_aluno(obj_aluno)
    return jsonify(aluno), 201

@aluno_controller.route('/<int:aluno_id>', methods=['GET'])
def obter_aluno(id):
    aluno = alunos_service.obter_aluno_por_id(id)
    if aluno:
        return jsonify(aluno)
    else:
        return jsonify({"error": "Aluno não encontrado"}), 404

@aluno_controller.route('/<int:aluno_id>', methods=['DELETE'])
def remover_aluno(aluno_id):
    sucesso = alunos_service.remover_aluno(aluno_id)
    if sucesso:
        return jsonify(sucesso), 200
    else:
        return jsonify({"error": "Aluno não encontrado"}), 404
    
@aluno_controller.route('/', methods=['PUT'])
def atualizar_aluno():
    dados = request.get_json()
    obj_aluno = Aluno(id=dados['id'], nome=dados['nome'], rm=dados['rm'], cpf=dados['cpf'], idade=dados['idade'])
    aluno = alunos_service.atualizar_aluno(obj_aluno)
    if aluno:
        return jsonify(aluno)
    else:
        return jsonify({"error": "Aluno não encontrado"}), 404