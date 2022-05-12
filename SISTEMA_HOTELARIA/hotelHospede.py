from datetime import date
from time import sleep

dicionario = {}
lista = []

class cadastroHospede():
    def __init__(self):
        pass
    def salvarCadastro(self):
        dicionario[int(input("Digite CPF: "))] = str(input("Digite nome: "))  
        lista.append(dicionario)   
        return print(lista)
        #sleep(3)
        #print(f"\n##### Nome: {self.nomeHospede}")
        #print(f"\n##### CPF:  {self.cpfHospede}")
        #print(f"\n##### Data: {self.dataHospede}")
        #print("\n------------------------------------------------------")
        
print("\n### HOTEL-TUPI-GUARANI ###\n")

hospede = cadastroHospede()
#usar um while, com a seguinte notação 'v == 's''
for i in range(2): 
    hospede.salvarCadastro()
