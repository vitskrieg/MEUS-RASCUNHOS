from datetime import date
from time import sleep

class hotelHospede():
    def __init__(self,nomeHospede, cpfHospede, dataHospede):
        self.nomeHospede = nomeHospede
        self.cpfHospede = cpfHospede
        self.dataHospede = dataHospede

    def cadastroHospede(self):
        sleep(3)
        print(f"\n##### Nome: {self.nomeHospede}")
        print(f"\n##### CPF:    {self.cpfHospede}")
        print(f"\n##### Data:    {self.dataHospede.date('%d/%m/%Y')}")
        print("\n------------------------------------------------------")
        
        botao1 = str(input("\nTudo certo com seu cadastro ? [s/n]"))

        if botao1 == 's':
            print("Salavando cadastro...")
            sleep(3)
            return print("HOSPEDE CADASTRADO !!!!\n")
        else:
            return print("Tente novamente do inicio")


print("\n### HOTEL-TUPI-GUARANI ###\n")

d1 = input("---INFORME NOME: ")
d2 = input("\n---INFORME CPF: ")
d3 = str(input("\n---INFORME DATA DE NASCIMENTO: "))

hospede1 = hotelHospede(d1,d2,d3)
hospede1.cadastroHospede()
