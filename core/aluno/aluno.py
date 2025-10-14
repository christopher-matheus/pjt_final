class Aluno:
    def __init__(self, nome, id, rm):
        self.nome = nome
        self.id = id
        self.rm = rm

@property
def nome(self):
    return self.__nome
@nome.setter
def nome(self, nome):
    self.__nome = nome


@property
def id(self):
    return self.__id  
@id.setter
def set_id(self, id):
    self.__id = id


@property
def rm(self):
    return self.__rm 
@rm.setter
def set_rm(self, rm):
    self.__rm = rm 