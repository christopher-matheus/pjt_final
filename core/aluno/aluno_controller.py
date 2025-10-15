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
    obj_aluno = Aluno(id=0, nome=dados['nome'], rm=dados['rm'])
    alunos_service.adicionar_aluno(obj_aluno)