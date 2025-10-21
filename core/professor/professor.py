class Professor:
    def __init__(self, nome, id, disciplina):
        self.nome = nome
        self.id = id
        self.disciplina = disciplina


    @property
    def usuario(self):
        return self._usuario
    @usuario.setter
    def usuario(self, n_usuario):
        self._usuario = n_usuario


    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, n_id):
        self._id = n_id


    @property
    def disciplina(self):
        return self._disciplina 
    @disciplina.setter
    def disciplina(self, n_disciplina):
        self._disciplina = n_disciplina