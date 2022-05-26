import pandas as pd

dados = pd.read_csv(r'C:\Users\aluno08\Documents\CETAM\Aulas\Modulo_3\Vilson_VsCode2\aula03\aluguel.csv', sep = ';')


#print(dados)

organizando_valores = dados[['Tipo', 'Bairro', 'Condominio', 'IPTU','Valor' ]]
#print(organizando_valores)

organizando_valores.sort_values('Valor', inplace=True, ascending=False)
print(organizando_valores)

organizando_valores = organizando_valores[['Tipo', 'Bairro', 'Valor']]
print(organizando_valores)

