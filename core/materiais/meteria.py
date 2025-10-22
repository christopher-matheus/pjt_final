class Materia:
    def __init__(self, id, nome, descricao, sg_crc):
        self.sg_crc = sg_crc
        self.id = id
        self.nome = nome
        self.descricao = descricao

    @property
    def sg_crc(self):
        return self._sg_crc
    @sg_crc.setter
    def sg_crc(self, n_sg_crc):
        self._sg_crc = n_sg_crc


    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, n_id):
        self._id = n_id


    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, n_nome):
        self._nome = n_nome

        
    @property
    def descricao(self):
        return self._descricao
    @descricao.setter
    def descricao(self, n_descricao):
        self._descricao = n_descricao
    