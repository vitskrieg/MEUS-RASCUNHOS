import pandas as pd
import matplotlib.pyplot as plt
#tiposdeimoveis

dados = pd.read_csv(r'C:\Users\aluno08\Documents\CETAM\Aulas\Modulo_3\Vilson_VsCode2\aula03\aluguel.csv', sep=';')
print(dados)

#o nome da coluna pode ser a chave
# da coluna
tipos_de_imoveis = dados['Tipo']
print(tipos_de_imoveis)
#o dado da coluna é do tipo 'Series'
print(type(tipos_de_imoveis))

#remove uma coluna
tipos_de_imoveis.drop_duplicates(inplace=True)
print(tipos_de_imoveis)

print(tipos_de_imoveis.index)
print(tipos_de_imoveis.shape[0])

tipos_de_imoveis.index = range(tipos_de_imoveis.shape[0])
print(tipos_de_imoveis)

#
grafico = dados[:5]['Valor']
plt.plot(grafico)
x = range(grafico.shape[0])
plt.plot(grafico)
plt.show()

#Exportando base de dados

tipos_de_imoveis.to_csv(r'C:\Users\aluno08\Documents\CETAM\Aulas\Modulo_3\Vilson_VsCode2\aula03\aluguel.csv', sep=';', index= False)