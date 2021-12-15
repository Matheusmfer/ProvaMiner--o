'1 - Utilizando a base de dados em csv titanic(https://github.com/pandas-dev/pandas/blob/master/doc/data/titanic.csv) resolva:
'a) Mostre as 10 primeiras entradas
'b) Organize a base de dados em ordem alfabética por nome
'c) Crie uma nova série(no mesmo dataframe) com o nome "Sobrevivente", o conteúdo deve ser "Sim" caso a coluna Survived for 1 e "Não" caso a coluna Survived for 0
'd) Remova as colunas "SibSp", "Parch" e "Ticket"
'e) Renomeie as colunas restantes para sua tradução em português
'f) Altere os valores da coluna Sexo para: male = "masculino"(minúsculas) e female = "FEMININO"(maiúsculas)
'g) Apresente o número de sobreviventes por classe
'h) Apresente o número de mortos por sexo
'i) Monte um gráfico(formato a sua escolha) que mostre o número de sobreviventes por classe
'j) Exporte seu dataframe para um arquivo com extensão XLSX'

'1 - Utilizando a base de dados em csv titanic(https://github.com/pandas-dev/pandas/blob/master/doc/data/titanic.csv) resolva:
'a) Mostre as 10 primeiras entradas
'b) Organize a base de dados em ordem alfabética por nome
'c) Crie uma nova série(no mesmo dataframe) com o nome "Sobrevivente", o conteúdo deve ser "Sim" caso a coluna Survived for 1 e "Não" caso a coluna Survived for 0
'd) Remova as colunas "SibSp", "Parch" e "Ticket"
'e) Renomeie as colunas restantes para sua tradução em português
'f) Altere os valores da coluna Sexo para: male = "masculino"(minúsculas) e female = "FEMININO"(maiúsculas)
'g) Apresente o número de sobreviventes por classe
'h) Apresente o número de mortos por sexo
'i) Monte um gráfico(formato a sua escolha) que mostre o número de sobreviventes por classe
'j) Exporte seu dataframe para um arquivo com extensão XLSX'

import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('titanic.csv')
titanic = titanic.drop(columns=['SibSp'])
titanic = titanic.drop(columns=['Parch'])
titanic = titanic.drop(columns=['Ticket'])

titanic = titanic.rename(columns = {'PassengerId': 'IdPassageiro', 'Survived': 'Sobrevivnetes', 'Pclass':'ClasseP', 'Name':'Nome','Sex':'Sexo', 'Age':'Idade', 'Fare':'Tarifa', 'Cabin':'Cabine', 'Embarked':'Embarcou'}, inplace = False)

titanic = titanic.head(10)

print(titanic)