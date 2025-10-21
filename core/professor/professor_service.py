from core.professor.professor_repository import ProfessorRepository
from core.professor.professor import Professor
class professorService:

    def __init__(self):
        self.repository = ProfessorRepository()

    def listar_professors(self):
        return self.repository.listar()
    
    def adicionar_professor(self, professor):
        if isinstance(professor, Professor):
            return self.repository.adicionar(professor)
        else:
            return None
    def atualizar_professor(self, professor):
        if isinstance(professor, professor):
            if professor.id > 0:
                return self.repository.atualizar(professor)
            else:
                return "Id do professor é obrigatório para a atualização"
        else:
            return None
    def remover_professor(self, professor_id):
        sucesso = self.repository.remover(professor_id)
        if not sucesso:
            return None
        else:
            return {"id": professor_id, "professor removido com sucesso": True}
        
    def obter_professor_por_professor_e_senha(self, professor, senha):
        professor = self.repository.obter_por_id(professor, id)
        if not professor:
            return None
        else:
            return professor