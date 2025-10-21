class Professor:
    def __init__(self, nome, id, formacao, cpf, idade):
        self.nome = nome
        self.id = id
        self.idade = idade
        self.cpf = cpf
        self.formacao = formacao


    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, n_nome):
        self._nome = n_nome
    
    
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, n_idade):
        self._idade = n_idade


    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, n_cpf):
        self._cpf = n_cpf


    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, n_id):
        self._id = n_id


    @property
    def formacao(self):
        return self._formacao 
    @formacao.setter
    def formacao(self, n_formacao):
        self._formacao = n_formacao