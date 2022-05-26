import pandas as pd

dados = pd.read_csv(r'C:\Users\aluno08\Documents\CETAM\Aulas\Modulo_3\Vilson_VsCode2\aula03\aluguel.csv', sep=';')

selecao1 = dados['Tipo'] == 'Apartamento'
print(selecao1)

#variavel que recebera o tamanho de todos que retornaram como 'True' na seleção
#n1 = dados[selecao1].shape[0]
#print(n1)

n1 = dados[selecao1].shape[0]
print('Numero de apartamentos',n1)

selecao2 = (dados['Tipo'] == 'Casa') | (dados['Tipo'] == 'Casa de Condominio') | (dados['Tipo'] == 'Casa de Vila')

n2 = dados[selecao2].shape[0]
print("Numeros de Casas, Casa de Condominio e Casas de Vila é:  ", n2)

selecao3 = ((dados['Area'] >= 60) & (dados['Area'] <=100))
n3 = dados[selecao3].shape[0]

print("Terrenos com mais de 60 e menos de 100: ", n3)

selecao4 = ((dados['Quartos'] >= 4)&(dados['Valor'] <= 2000))
n4 = dados[selecao4].shape[0]

print("Questão 4: ", n4)