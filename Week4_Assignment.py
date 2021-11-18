import pandas as pd
import numpy as np
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN':'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

def get_list_of_university_towns():
    file1 = pd.read_csv('university_towns.txt',sep='/n',header=None)
    file = file1.rename(columns={0:'State'})
    States_Regions = []
    for i in range(0,len(file)):
        if "[edit]" in (file.loc[i,'State']):
            State = (file.loc[i,'State'][:-7])
        elif '(' in (file.loc[i,'State']):
            RegionName = file.loc[i,'State'][: file.loc[i,'State'].index('(') - 1]

            States_Regions.append([State, RegionName])

    dataframe = pd.DataFrame(States_Regions,columns = ['State','RegionName'])
    return dataframe

gdp = pd.read_excel("gdplev.xlsx", header=7)
gdp=gdp[['Unnamed: 4','Unnamed: 5','Unnamed: 6']]
gdp=gdp.rename(columns={'Unnamed: 4':'year_quarter','Unnamed: 5':'current','Unnamed: 6':'chained'})
gdp = gdp[gdp.year_quarter >= "2000q1"].reset_index()
gdp=gdp.drop(columns=['index'])

def get_recession_start():
    for i in range(2, len(gdp)):
        if (gdp.loc[i-2,'current'] > gdp.loc[i-1,'current']) and (gdp.loc[i-1,'current'] > gdp.loc[i,'current']):
            return (gdp.loc[i-2,'year_quarter'])

def get_recession_end():
    gdp = pd.read_excel("gdplev.xlsx", header=7)
    gdp=gdp[['Unnamed: 4','Unnamed: 5','Unnamed: 6']]
    gdp=gdp.rename(columns={'Unnamed: 4':'year_quarter','Unnamed: 5':'current','Unnamed: 6':'chained'})
    gdp = gdp[gdp.year_quarter >= "2000q1"].reset_index()
    gdp=gdp.drop(columns=['index'])
    start_recession = get_recession_start()
    start_index = gdp[gdp['year_quarter'] == start_recession].index[0]
    gdp = gdp.iloc[start_index:]
    for i in range(2, len(gdp)):
        if (gdp.iloc[i-2][1] < gdp.iloc[i-1][1]) and (gdp.iloc[i-1][1] < gdp.iloc[i][1]):
            return gdp.iloc[i][0]

def get_recession_bottom():
    gdp = pd.read_excel("gdplev.xlsx", header=7)
    gdp=gdp[['Unnamed: 4','Unnamed: 5','Unnamed: 6']]
    gdp=gdp.rename(columns={'Unnamed: 4':'year_quarter','Unnamed: 5':'current','Unnamed: 6':'chained'})
    gdp = gdp[gdp.year_quarter >= "2000q1"].reset_index()
    gdp=gdp.drop(columns=['index'])
    start_recession = get_recession_start()
    start_ind = gdp[gdp['year_quarter'] == start_recession].index[0]
    end_recession   = get_recession_end()
    end_ind = gdp[gdp['year_quarter'] == end_recession].index[0]
    minimum,min_index = gdp.iloc[start_ind]['current'],start_ind
    for i in range(start_ind,end_ind+1):
        if (gdp.loc[i,'current'] < minimum):
            min_index = i
            minimum = gdp.loc[i,'current']
    recession_bottom = gdp.iloc[min_index]['year_quarter']
    return recession_bottom

print(get_list_of_university_towns())
print(get_recession_start())
print(get_recession_end())
print(get_recession_bottom())