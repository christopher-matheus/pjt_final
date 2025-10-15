from flask import Blueprint, request, jsonify
from core.aluno.aluno_service import AlunoService

aluno_controller = Blueprint('aluno', __name__, url_prefix='/alunos')

alunos_service = AlunoService()

@aluno_controller.route('/', methods=['GET'])
def listar_alunos():
    alunos = alunos_service.listar_alunos()
    return jsonify(alunos)
