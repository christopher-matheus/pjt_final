class Usuario:
    def __init__(self, nome, id, email):
        self.nome = nome
        self.id = id
        self.email = email

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, valor):
        self._nome = valor


    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, valor):
        self._id = valor

        
    @property
    def email(self):
        return self._email 
    @email.setter
    def email(self, valor):
        self._email = valor