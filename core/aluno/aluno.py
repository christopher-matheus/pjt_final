class Aluno:
    def __init__(self, nome="", id=0, rm=0, cpf="", idade=0):
        self.nome = nome
        self.id = id
        self.rm = rm
        self.cpf = cpf
        self.idade = idade

@property
def nome(self):
    return self.__nome
@nome.setter
def nome(self, new_nome):
    self.__nome = new_nome


@property
def id(self):
    return self.__id  
@id.setter
def set_id(self, new_id):
    self.__id = new_id


@property
def rm(self):
    return self.__rm 
@rm.setter
def set_rm(self, new_rm):
    self.__rm = new_rm 
    
@property
def cpf(self):
    return self.__cpf 
@cpf.setter
def set_cpf(self, new_cpf):
    self.__cpf = new_cpf


@property
def idade(self):
    return self.__idade  
@idade.setter
def set_idade(self, new_idade):
    self.__idade = new_idade