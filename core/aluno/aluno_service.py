from core.aluno.aluno_repository import AlunoRepository
class AlunoService:

    def __init__(self):
        self.repository = AlunoRepository

    def listar_alunos(self):
        return self.repository.listar()