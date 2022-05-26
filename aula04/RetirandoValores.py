import pandas as pd

#'&' significa E
# '|' significa OU

dados = pd.read_csv(r"C:\Users\aluno08\Documents\CETAM\Aulas\Modulo_3\Vilson_VsCode2\aula04\aluguel.csv", sep=';')

#fatiando e mostrando
print(dados[:10].head())

#retorna "False" para valores não nulos
print(dados.isnull())

#mostra a quantidade de dados
print(dados.info())

print(dados[dados['Valor'].isnull()])

#tamanho da tabela
a = dados.shape[0]
print(a)
print(' ')

#tirando valores nulos
dados.dropna(subset=['Valor'], inplace= True)
b = dados.shape[0]
print(' ')
print(b)

#imprima a quantidade eliminada
print(' ')
print("Quantidade eliminada igual a: ", a-b)
print("")

selecao = (dados['Tipo'] == 'Apartamentos') & (dados['Condominio'].isnull())
c = dados.shape[0]
print(c)

#'~' inverte o isnull, agora quando for nulo retorna False e se tiver valor retorna True
dados = dados[~selecao]
d = dados.shape[0]
print(d)

print(c-d)

dados.fillna(0, inplace = True)
print(dados['Condominio'])

dados.to_csv(r"C:\Users\aluno08\Documents\CETAM\Aulas\Modulo_3\Vilson_VsCode2\aula04\tipos_de_hugo.csv", sep=';', index = False)