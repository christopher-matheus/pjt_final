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
    def sg_crc(self, new_sg_crc):
        self._sg_crc = new_sg_crc


    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, new_id):
        self._id = new_id


    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, new_nome):
        self._nome = new_nome


    @property
    def descricao(self):
        return self._descricao
    @descricao.setter
    def descricao(self, new_descricao):
        self._descricao = new_descricao
    