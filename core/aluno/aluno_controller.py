from flask import Blueprint, request, jsonify

aluno_controller = Blueprint('aluno', __name__, url_prefix='/alunos')

@aluno_controller.route('/', methods=['GET'])
def listar_alunos():
    pass
    