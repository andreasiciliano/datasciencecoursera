import pandas as pd
import numpy as np

skip_rows = [i for i in range(0,18)]
labels = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
usecols = [2,3,4,5]
energy = pd.read_excel('Energy Indicators.xls', header = None, skiprows = skip_rows, skip_footer = 38, usecols=usecols, names = labels)

country_dict = {
    'Republic of Korea':'South Korea',
    'United States of America20': 'United States',
    'United Kingdom of Great Britain and Northern Ireland19': 'United Kingdom',
    'China, Hong Kong Special Administrative Region3': 'Hong Kong',
    'China, Macao Special Administrative Region4': 'Macao',
    'Australia1': 'Australia',
    'Bolivia (Plurinational State of)': 'Bolivia',
    'China2': 'China',
    'Denmark5': 'Denmark',
    'Falkland Islands (Malvinas)': 'Falkland Islands',
    'France6': 'France',
    'Greenland7': 'Greenland',
    'Indonesia8': 'Indonesia',
    'Iran (Islamic Republic of)': 'Iran',
    'Italy9': 'Italy',
    'Japan10': 'Japan',
    'Kuwait11': 'Kuwait',
    'Micronesia (Federated States of)': 'Micronesia',
    'Netherlands12': 'Netherlands',
    'Portugal13': 'Portugal',
    'Saudi Arabia14': 'Saudi Arabia',
    'Serbia15': 'Serbia',
    'Sint Maarten (Dutch part)': 'Sint Maarten',
    'Spain16': 'Spain',
    'Switzerland17': 'Switzerland',
    'Ukraine18': 'Ukraine',
    'Venezuela (Bolivarian Republic of)': 'Venezuela',
	}

energy = energy.replace(to_replace = {'Country':country_dict, 'Energy Supply': {'...': np.NaN}})
energy['Energy Supply'] = energy['Energy Supply']*1E6
#print([s for s in energy['Country'].tolist() if 'orea' in s])


# GDP Data
gdp = pd.read_csv('world_bank.csv', skiprows=4)
gdp = gdp.rename(columns={'Country Name': 'Country'})
gdp = gdp[['Country', '2006', '2007', '2008','2009','2010', '2011','2012','2013','2014','2015']]

country_dict_gdp = {
    'Korea, Rep.': 'South Korea',
    'Iran, Islamic Rep.': 'Iran',
    'Hong Kong SAR, China': 'Hong Kong'}

gdp = gdp.replace(to_replace = {'Country':country_dict_gdp})
#print([s for s in gdp['Country'].tolist() if 'orea' in s])

#ScimEn
ScimEn = pd.read_excel('scimagojr-3.xlsx')
