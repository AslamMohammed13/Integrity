import pandas as pd
import numpy as np


def final_data():
    energy = pd.ExcelFile('Energy Indicators.xlsx').parse(skiprows=17, skip_footer=(38))
    energy = energy[['Unnamed: 2', 'Petajoules', 'Gigajoules', '%']]
    energy = energy.rename(
        columns={'Unnamed: 2': 'Country', 'Petajoules': 'Energy Supply', 'Gigajoules': 'Energy Supply per Capita',
                 '%': '% Renewable'})
    energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']] = energy[
        ['Energy Supply', 'Energy Supply per Capita', '% Renewable']].replace('...', np.NaN)
    energy['Energy Supply'] = pd.to_numeric(energy['Energy Supply'])
    energy['Energy Supply per Capita'] = pd.to_numeric(energy['Energy Supply per Capita'])
    energy['% Renewable'] = pd.to_numeric(energy['% Renewable'])
    energy['Energy Supply'] = 1000000 * energy['Energy Supply']
    energy['Country'] = energy['Country'].replace({'China, Hong Kong Special Administrative Region': 'Hong Kong',
                                                   'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
                                                   'Republic of Korea': 'South Korea',
                                                   'United States of America': 'United States',
                                                   'Iran (Islamic Republic of)': 'Iran'})

    energy['Country'] = energy['Country'].str.replace('\d+', '')

    # Assumption- The country names are to be changed manually as the description doesnt form complete solution to fetch US and UK from energy dataset
    energy.loc[216, 'Country'] = 'United States'
    energy.loc[214, 'Country'] = 'United Kingdom'

    GDP = pd.read_csv('world_bank.csv', skiprows=4)
    GDP['Country Name'] = GDP['Country Name'].replace(
        {'Korea, Rep.': 'South Korea', 'Iran, Islamic Rep.': 'Iran', 'Hong Kong SAR, China': 'Hong Kong'})
    GDP = GDP[['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    GDP = GDP.rename(columns={'Country Name': 'Country'})

    ScimEn = pd.read_excel('scimagojr-3.xlsx')
    ScimEn = ScimEn[:15]
    energy_scimen = pd.merge(ScimEn, energy, how='inner', left_on='Country', right_on='Country')
    final = pd.merge(energy_scimen, GDP, how='inner', left_on='Country', right_on='Country')

    return final

final = final_data()
def second():
    a= final[['Country','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']]
    a=a.replace(np.nan,0,regex=True)
    list_years= ['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
    list_avg=[]
    for i in range(0,len(a)):
        sum =0
        for j in list_years:
            sum = sum + a.loc[i,j]
        list_avg.append(sum)
    list_countries=a['Country']
    df = pd.DataFrame({'Country':list_countries,'Average_GDP':list_avg})
    return df

exec(f'second = second()')


def third():
    country = second.sort_values(by='Average_GDP', ascending=False).reset_index().loc[5, 'Country']
    index = final.index[final['Country'] == country].tolist()[0]
    difference = final.loc[index, '2015'] - final.loc[index, '2006']

    return difference

def fourth():
    return final['Energy Supply per Capita'].mean()

def fifth():
    index=final['% Renewable'].sort_values(ascending=False).idxmax()
    return final.loc[index,'Country']

def sixth():
    final['Self-citations/Citations'] = final['Self-citations']/final['Citations']
    index=final['Self-citations/Citations'].sort_values(ascending=False).idxmax()
    print('the maximum values is',final['Self-citations/Citations'].sort_values(ascending=False)[0])
    return final.loc[index,'Country']

def seventh():
    final['population'] = final['Energy Supply']/final['Energy Supply per Capita']
    index=final['population'].sort_values(ascending=False).index[2]
    return final.loc[index,'Country']

def eight():
    final['citable documents per person'] = final['Citable documents']/final['population']
    corr=final[['citable documents per person','Energy Supply per Capita']].corr(method='pearson').iloc[0,1]
    return corr

def ninth():
    for i in range(0,len(final)):
        if final.loc[i,'% Renewable'] > final['% Renewable'].median():
            final['new_renewable']=1
        else:
            final['new_renewable']=0
    return final

def tenth():
    continents = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}
    final['Continent'] = None
    for i in range(len(final)):
        final.loc[i,'Continent']= continents[final.loc[i,'Country']]
        final['bins'] = pd.cut(final['% Renewable'],5)
    return final.groupby(['Continent','bins']).size()

def eleventh():
    for i in range(len(final)):
        final.loc[i,'PopEstimate_commas'] = format(final.loc[i,'population'],",")
    return final

print("----------Answer 1-------------")
print(final_data())
print("----------Answer 2-------------")
print(second)
print("----------Answer 3-------------")
print(third())
print("----------Answer 4-------------")
print(fourth())
print("----------Answer 5-------------")
print(fifth())
print("----------Answer 6-------------")
print(sixth())
print("----------Answer 7-------------")
print(seventh())
print("----------Answer 8-------------")
print(eight())
print("----------Answer 9-------------")
print(ninth())
print("----------Answer 10-------------")
print(tenth())
print("----------Answer 11-------------")
print(eleventh())

