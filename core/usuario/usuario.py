class Usuario:
    def __init__(self, nome, id, ativo, senha):
        self.nome = nome
        self.id = id
        self.senha = senha
        self.ativo = ativo

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, n_nome):
        self._nome = n_nome


    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, n_id):
        self._id = n_id


    @property
    def ativo(self):
        return self._ativo 
    @ativo.setter
    def ativo(self, n_ativo):
        self._ativo = n_ativo

    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self, n_senha):
        self._senha = n_senha