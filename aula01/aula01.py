import pandas as pd

"""
mydataset = {
    'carros': ['BMW','Volvo','Ford'],
    'passageiro': [2,3,5]
}

mostrar = pd.DataFrame(mydataset)

print(mostrar)
"""

wilson = pd.read_csv(r'C:\Users\aluno08\Documents\CETAM\Aulas\Modulo_3\Vilson_VsCode2\aula_01_modulo_3\transferencia.csv', sep=';')
print(wilson)
print(wilson['Município'])

# print(wilson[inicio: ate onde: passo])=
print(wilson[:3])

hugo = wilson[['Município', 'Ação Orçamentária']]
print(hugo)
print(hugo['Município'][200])

print(hugo.info())
print(wilson.info())

filtro_hugo = hugo.drop(['Ação Orçamentária'], axis=1)
print(filtro_hugo)

Location = wilson[["UF","Município"]]
verba = wilson[["Ação Orçamentária","Valor Transferido"]]
