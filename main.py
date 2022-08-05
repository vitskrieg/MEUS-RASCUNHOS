from keras.models import load_model
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix
from sklearn.neural_network import MLPClassifier
import pickle

"""
'Age', 'Gender', 'self_employed', 'family_history', 'work_interfere',
       'no_employees', 'remote_work', 'tech_company', 'benefits',
       'care_options', 'wellness_program', 'seek_help', 'anonymity', 'leave',
       'mental_health_consequence', 'phys_health_consequence', 'coworkers',
       'supervisor', 'mental_health_interview', 'phys_health_interview',
       'mental_vs_physical', 'obs_consequence', 'age_range'
"""

with open(r'C:\Users\aluno23\Documents\vilson filho\survey (1).pkl','rb') as f:
  X_train, X_test, X_valid,y_train, y_test, y_valid = pickle.load(f)

print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)
print(X_valid.shape, y_valid.shape)

rede_neural = pickle.load(open(r'C:\Users\aluno23\Documents\vilson filho\survey_redeneural (1).sav','rb'))
arvore = pickle.load(open(r'C:\Users\aluno23\Documents\vilson filho\survey_arvore (1).sav','rb'))
naivybaes = pickle.load(open(r'C:\Users\aluno23\Documents\vilson filho\survey_naivy (1).sav','rb'))

print('\n\n')
print("############################################################################")
print("#####                     DIAGNÓSTICO DE DOENÇA MENTAL                #####")
print("############################################################################")
loop = int(input("# Digite para iniciar o diagnóstico:  0 - FIM | 1 - INICIAR: \n# "))
while loop != 0:
  #input('# Bote aqui: ')
  Gender = input('# Bote aqui: \n')
  self_employed = input('# Bote aqui: \n')
  family_history = input('# Bote aqui: \n')
  benefits = input('# Bote aqui: \n')
  care_options = input('# Bote aqui: \n')
  anonymity = input('# Bote aqui: \n')
  leave = input('# Bote aqui: \n')
  work_interfere = input('# Bote aqui: \n')
   

  previsores = arvore.predict([[Gender,self_employed,family_history,benefits,care_options,anonymity,leave,work_interfere]])
  previsores

  if previsores == 0:
    print('\n# Paciente diagnosticado como não diabetico.\n')
    print("############################################################################")

  elif previsores == 1:
    print('\n# Paciente diagnosticado como diabetico.\n')
    print("############################################################################")

    loop = int(input("\n# Digite para iniciar o diagnóstico:  0 - FIM | 1 - CONTINUAR: \n# "))
    print("############################################################################\n")

previsores = arvore.predict(X_test)
previsores_2 = naivybaes.predict(X_test)
previsores_3 = rede_neural.predict(X_test)

print(accuracy_score(y_test, previsores))
print(accuracy_score(y_test, previsores_2))
print(accuracy_score(y_test, previsores_3))