import pandas as pd
import numpy as np

data = pd.read_csv("bank.csv",sep=';')

#Question 1
print("-----------------------------------Answer 1-----------------------------------")
average_balance =  pd.DataFrame(data.groupby(['age']).balance.mean())
average_balance.rename(columns={'age':'count'}, inplace=True)
print(average_balance)

#Question 2
print("-----------------------------------Answer 2-----------------------------------")
df=data[data['loan']=='yes']
print("Age with highest loan is:",pd.DataFrame(df.groupby('age').count()['loan']).idxmax()['loan'])

#Question 3
print("-----------------------------------Answer 3-----------------------------------")
max_age = data['age'].max()
bins = np.array([0,19,39,60,max_age])
groups = pd.DataFrame(data.groupby(pd.cut(data.age, bins)).count()['age'])
groups.rename(columns={'age':'count'}, inplace=True)
print(groups)

#Question 4
print("-----------------------------------Answer 4-----------------------------------")
average_balance =  pd.DataFrame(data.groupby(['job']).balance.mean())
average_balance.rename(columns={'job':'count'}, inplace=True)
print(average_balance)

#Question 5
print("-----------------------------------Answer 5-----------------------------------")
pd.set_option('display.max_rows', None)
average_balance =  pd.DataFrame(data.groupby(['job','age']).balance.mean())
print(average_balance)

#Question 6
print("-----------------------------------Answer 6-----------------------------------")
print("Age group having high impact on the campaign is:",data.groupby(['age']).sum()['campaign'].idxmax())

#Question 7
print("-----------------------------------Answer 7-----------------------------------")
print("Education group having high impact on the campaign is:",data.groupby(['education']).sum()['campaign'].idxmax())

