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

    def buscarContato(self, nome):
        nome = nome.lower()
        encontrado = False
        for i in self.contatos:
            if i['pessoa']['nome'] == nome:
                encontrado = True
                return(i)
        if encontrado == False:
            return "Nome não encontrado."

    def excluirContato(self, nome):
        nome = nome.lower()
        encontrado = False
        for i in self.contatos:
            if i['pessoa]']['nome'] == nome:
                encontrado = True
                self.contatos.remove(nome)
        if encontrado == False:
            return "Nome não encontrado."

    def salvar(self, contato):
        cont = open('Agenda.json', 'w')
        cont.write(contato)        
