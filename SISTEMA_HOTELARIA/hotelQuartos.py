

vagos= [{111: 'Vago'},{112:'Vago'},{113:'Vago'},{114:'Vago'},{115:'Vago'},{116:'Vago'},{117:'VAgo'},{118:'Vago'}]
naoVagos = []
class Quartos():
    def __init__(self) :
        pass
    
    def alugarQuarto(self):
        r2 = input("Deseja alugar um quarto ? s/n")
        while r2== 's':
            naoVagos.append(vagos.pop())
        print(naoVagos)

hospede = Quartos()
hospede.alugarQuarto()
hospede