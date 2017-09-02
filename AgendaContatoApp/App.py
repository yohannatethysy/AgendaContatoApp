import json
from Model.Telefone import Telefone
from Model.Contato import Contato
from Model.Agenda import Agenda
from Model.Pessoa import Pessoa


def para_dict(obj):
    if hasattr(obj, '__dict__'):
        obj = obj.__dict__
    if isinstance(obj, dict):
        return { k:para_dict(v) for k,v in obj.items() }
    elif isinstance(obj, list) or isinstance(obj, tuple):
        return [para_dict(e) for e in obj]
    else:
        return obj

def main():

    def incluirNovoContato():
   
        v = open("Agenda.json", "r", encoding='utf8')
        agendaJson = json.load(v)
        agenda = Agenda(agendaJson['proprietario'], agendaJson['contatos'])
        

        nome = input("Qual o nome do proprietário? ")
        nascimento = input("Qual a data de nascimento do proprietário? ")
        email = input("Qual o email do proprietário? ")

        pessoa = Pessoa(nome, nascimento, email)

        numero = input("Qual o numero do proprietário? ")
        ddd = input("Qual o ddd do proprietário? ")
        codPais = input("Qual o código do país do proprietário? ")

        telefone = Telefone(numero, ddd, codPais)

        contato = Contato(pessoa, telefone)
        agenda.incluirContato(contato)

        
        aJson = json.dumps(para_dict(agenda))

        v = open("Agenda.json", "w", encoding='utf8')

        v.write(aJson)

    def listarContatos():
        v = open("Agenda.json", "r", encoding='utf8')
        agendaJson = json.load(v)
        agenda = Agenda(agendaJson['proprietario'], agendaJson['contatos'])

        for contato in agenda.listarContatos():
            print(contato)

    def excluirContatos():
        v = open("Agenda.json", "r", encoding='utf8')
        agendaJson = json.load(v)
        agenda = Agenda(agendaJson['proprietario'], agendaJson['contatos'])

        nome = input("Qual o contato que deve ser deletado? ")
        agenda.excluirContato(nome)

        aJson = json.dumps(para_dict(agenda))

        v = open("Agenda.json", "w", encoding='utf8')

        v.write(aJson)

    def buscarContato():
        v = open("Agenda.json", "r", encoding='utf8')
        agendaJson = json.load(v)
        agenda = Agenda(agendaJson['proprietario'], agendaJson['contatos'])

        nome = input("Qual o nome do contato que você deseja buscar? ")
        agenda.buscarContato(nome)

    def contarContatos():
        pass


    try:
        v = open("Agenda.json", "r", encoding='utf8')
        print("Abrimos a agenda porque a encontramos :)")
    except FileNotFoundError:
        v = open("Agenda.json", "w", encoding='utf8')
        nome = input("Qual o nome do contato a ser adicionado? ")
        nascimento = input("Qual o nascimento do contato? ")
        email = input("Qual o email do contato? ")
        pessoa = Pessoa(nome, nascimento, email)
        a2 = Agenda(pessoa)
        a2Json = json.dumps(para_dict(a2))
        v.write(a2Json)
        print("Agenda criada.")

    print("Menu:\n "
            "1- Incluir contato\n"
            "2- Listar contatos\n"
            "3- Excluir contato\n"
            "4- Buscar contato\n"
            "5- Contar contatos\n"
            "6- Sair")

    try:
        op = input("Digite a opção desejada: ")

        if op == 1:
            incluirNovoContato()
        elif op == 2:
            listarContatos()
        elif op == 3:
            excluirContatos()
        elif op == 4:
            buscarContato()
        elif op == 5:
            contarContatos()
        elif op == 6:
            break

    except ValueError:
        print("Só números são válidos... Tente novamente!")


if __name__ == '__main__':
    main()
      
