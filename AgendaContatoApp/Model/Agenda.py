class Agenda():
    def __init__ (self, proprietario, contatos=[]):
        self.proprietario = proprietario
        self.contatos = contatos

    def contarContatos(self):
       return len(self.contatos)

    def listarContatos(self):
        return self.contatos
        
    def incluirContato(self, contato):
        self.contatos.append(contato)
