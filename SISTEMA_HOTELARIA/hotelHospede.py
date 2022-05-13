from datetime import date
from time import sleep

dicionario = {}
lista = []

class cadastroHospede():
    def __init__(self):
        pass
    def salvarCadastro(self,cpf):
        dicionario[int(cpf)] = str(input("Digite nome: "))  
        lista.append(dicionario)   
        return print(lista)
        

print("\n### HOTEL-TUPI-GUARANI ###\n")
hospede = cadastroHospede()

#usar um while, com a seguinte notação 'v == 's''
r = str(input("Deseja adicionar outro hospede ? s/n"))
while r == 's':
    hospede.salvarCadastro()
