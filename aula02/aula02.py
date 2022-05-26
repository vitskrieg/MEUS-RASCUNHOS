from tarfile import CompressionError
import pandas as pd

#criando Planilhas

df = pd.DataFrame({
    'name':['Raphael','Donatello'],
    'Mask':['Red','Green'],
    'Idade':[12, 20]
})

df.to_csv(index=True)

print(df)

#criando um zip
compri = dict(method='zip', 
            archive_name='Df.csv')
df.to_csv('Df.zip', index=False, compression=compri)

df_2 = pd.read_csv('C:\Users\aluno08\Documents\CETAM\Aulas\Modulo_3\Vilson_VsCode2\aula_01_modulo_3\aula02\Df.csv',sep=',')
print(df_2)