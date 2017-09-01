cimport datetime

class Contato():
    def __init__(self, pessoa, telefone):
        self.criacao = str(datetime.date.today())
        self.pessoa = pessoa
        self.telefone = telefone

    def listarTelefones(self):
        pass
