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
        ####### Refazer #######
        # Carregando
        v = open("Agenda.json", "r", encoding='utf8')
        agendaJson = json.load(v)
        agenda = Agenda(agendaJson['proprietario'], agendaJson['contatos'])
        ######## Refazer #######

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

        ###### Refazer #######
        # Salvando
        aJson = json.dumps(para_dict(agenda))

        v = open("Agenda.json", "w", encoding='utf8')

        v.write(aJson)
        ##### Refazer #######
