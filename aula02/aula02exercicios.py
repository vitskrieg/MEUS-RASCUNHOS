from mailbox import NotEmptyError
import pandas as pd

nome = []
idade = []
cpf = []
bairro = []
cidade = []
estado = []

for i in range(2):
    d1 = str(input("\nNome: "))
    d2 = int(input("\nIdade: "))
    d3 = int(input("\nCPF: "))
    d4 = str(input("\nBairro: "))
    d5 = str(input("\nCidade: "))
    d6 = str(input("\nEstado: "))
    nome.append(d1),
    idade.append(d2),
    cpf.append(d3),
    bairro.append(d4),
    cidade.append(d5),
    estado.append(d6)



df2 = pd.DataFrame({
    'Nome':nome,
    'Idade':idade,
    'CPF':cpf,
    'Bairro':bairro,
    'Cidade':cidade,
    'Estado':estado
})

df2.to_csv(index=True)
print(df2)

#compri = dict(method='zip',
#            archive_name='Df2.csv')
#df2.to_csv('Df2.zip', index=False, compression=compri)

