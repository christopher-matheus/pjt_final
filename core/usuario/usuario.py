class Usuario:
    def __init__(self, usuario, id, ativo, senha):
        self.usuario = usuario
        self.id = id
        self.senha = senha
        self.ativo = ativo

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