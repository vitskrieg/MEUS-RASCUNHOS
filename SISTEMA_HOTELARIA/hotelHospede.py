from datetime import date
from time import sleep

dicionario = {}
lista = []

class cadastroHospede():
    def __init__(self):
        pass

    def salvarCadastro(self):
        cpf  = input("\n#####  Informe seu cpf:  ")
        nome = input("\n#### Informe seu nome")
        dicionario[str(cpf)] = str(nome)  
        lista.append(dicionario)   
        return print(lista)        

print("\n### HOTEL-TUPI-GUARANI ###\n")
hospede = cadastroHospede()

r = str(input("Deseja adicionar outro hospede ? s/n  "))
while r  == ' s ' :
    hospede.salvarCadastro()