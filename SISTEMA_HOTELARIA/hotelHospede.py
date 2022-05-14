hospedes = {}
quartosVagos = {'112':'Quarto 1' ,'113':'Quarto 2','114':'Quartos 3' ,'115':'Quartos 4','116':'Quartos 5','117':'Quarto 6'}
quartosReservados = {}
conta = []

class cadastroHospede():
    def __init__(self):
        pass

    #Salvar Cadastro Cliente
    def salvarCadastro(self,cpf,nome):
        hospedes[cpf] = nome
        return print(hospedes)
        return hospedes
    
    #Alugar quarto
    def quartosHospede(self,b):
      
      if b =='112':
        quartosReservados = quartosVagos['112']
        print("Quarto 1: RESERVADO")
        preco = 500.0
      elif b =='113':
        quartosReservados = quartosVagos['113']
        print("Quarto 2: RESERVADO")
        preco = 550.0

      elif b =='114':
        quartosReservados = quartosVagos['114']
        print("Quarto 3: RESERVADO")
        preco = 600.0
        
      elif b =='115':
        quartosReservados = quartosVagos['115']
        print("Quarto 4: RESERVADO")
        preco = 600.0

      elif b =='116':
        quartosReservados = quartosVagos['116']
        print("Quarto 5: RESERVADO")
        preco = 900.0      

      elif b =='117':
        quartosReservados = quartosVagos['117']
        print("Quarto 6: RESERVADO")
        preco = 900.0
      
      return preco

    #serviço DE QUARTO 
    def servico(self,opcao):
        
        if opcao =='1':
          print("Café da Manhã = R$ 30.0")
          Cafe_manha = 30.0
          return Cafe_manha
        
        elif opcao =='2':
          print("Almoço = R$ 50.0")
          Almoco =  50.0
          return Almoco

        elif opcao =='3':
          print("Lanche R$ = 30")
          Lanche = 35.0
          return Lanche
          
        elif opcao =='4':
          print("Jantar R$ = 60.0")
          Jantar = 60.0
          return Jantar 

        elif opcao =='0':
          print("Desistir")
          return Null
        else:
          return Null

        #EXECUÇÃO
        #############################################################################################################################

        print("\n### HOTEL-TUPI-GUARANI ###\n")
  
r = str(input("Adicionar hospede ? [s/n] ? "))

#SEÇÃO DE CADASTRO E SELEÇÃO DE QUARTOS
######################################################################################################

while (r == 's'):
    hospede = cadastroHospede()
    d1 = int(input("Insira seu cpf:---|  "))
    d2 = input("Insira seu nome:------|  ")
    d3 = int(input("Insira sua idade:-|  "))
    
    if d3 >= 18: 
      hospede.salvarCadastro(d1,d2)

      print('')
      print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
      print('')

      print(f"112-{quartosVagos['112']}:Economica 1 /R$ 500/ 1 cama de solteiro, um ventiladores, condicionador de ar, um banheiro, agua comum")
      print(f"113-{quartosVagos['113']}:Economica 2 /R$ 550/ 2 camas de solteiro, dois ventiladores, condicionador de ar, um banheiro, agua comum, toalha de cortesia")
      print(f"114-{quartosVagos['114']}:Mediana   1 /R$600/ 2 camas de solteiro, ar condicionado,toalhas quentes, agua quente")
      print(f"115-{quartosVagos['115']}:Mediana   2 /R$600/ 2 camas de solteiro, ar condicionado,toalhas quentes, agua quente")
      print(f"116-{quartosVagos['116']}:Executiva 1 /R$900/ 2 camas casal, ar split, frigobar, cinema, agua quente, banheiro")
      print(f"117-{quartosVagos['117']}:Executiva 2 /R$900/ 2 camas casal, ar split, frigobar, cinema, agua quente, banheiro")
      
      print('')
      print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
      print('')

      d4 = input('Escolha seu quarto:\n  ')
      hospede.quartosHospede(d4)
      valor = hospede.quartosHospede(d4)
      conta.append(valor)
      print(f"Seu aluguel: {valor}")
    else:
      print("Idade não permitida!!!!!!!!!!!\n")

    r = str(input("Adicionar outro hospede ? [s/n] ? \n"))

else:
  print('Encerrando...')

#SEÇÃO DE SERVIÇOS DE QUARTO

r2 = input("Deseja fazer um pedido ? [s/n]\n")

while r2 == 's':
  print("##### CARDAPIO DE SERVIÇOS ####")
  print("Opções: [1] Café da Manhã, [2] Almoço, [3]Lanche, [4]Jantar, [0]Desistir.")
  
  op =  input("Insira a opção desejada:  \n")
  hospede.servico(op)
  valor2 =  hospede.servico(op)
  conta.append(valor2)

  r2 = input("Deseja fazer outro pedido ? [s/n]\n")

else:
  print("Fechando sua conta...")
  pass

print(f"Sua conta atual:{conta}")

####CONTA (CHECKOUT)####

print("\n##### FECHAMENTO DE CONTA #####\n")

soma = sum(conta)

print(f"######  SEUS GASTOS: {contas}")
print(f"###### VALOR A PAGAR: {soma}")

print("MUITO OBRIGADO, VOLTE SEMPRE !!!!")