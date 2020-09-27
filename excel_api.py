# Data Preprocessing Template

# Importing the libraries
import numpy as np
import excel
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

import pandas as pd
from tablib import Dataset
import numpy as np
import matplotlib.pyplot as plt



# Importing the dataset
dataset = pd.read_csv('Data.xlsx', error_bad_lines=False)
#X = dataset.iloc[:, :-1].values
#y = dataset.iloc[:, -1].values
#dates_row = dataset.loc[4, :]
#xt = pd.Series(dates_row).values
nx = pd.read_excel('Data.xlsx')
df = pd.DataFrame(nx, columns= ['Name', 'P Number', 'age', 'love','python'])
Names = []
pNumbers = []
age = []
love = []
python = []

filtered_names = []
filtered_pNumbers = []
filtered_age = []
filtered_love = []
filtered_python = []

def show_table(names, numbers, ages, loves, pythons):
    for i in range(len(names)):
        print names[i] + " | " + numbers[i] + " | " +  ages[i] + "  | " + loves[i] + "  | " +  pythons[i]
        print "---------------------------------------------------------------"
        
for i in range(len(df['Name'])):
    #print df['Name'][i]
    Names.append(df['Name'][i])
    pNumbers.append(df['P Number'][i])
    age.append(df['age'][i])
    love.append(df['love'][i])
    python.append(df['python'][i])
print "Append to database one row values using forloop"
for x in range(len(Names)):
    name = str(Names[x])
    pr = str(pNumbers[x])
    m_age = str(age[x])
    m_love = str(love[x])
    m_python = str(python[x])
    
    #filter
    if name == 'nan':
        name = '------'
        filtered_names.append(name)
        
    else:
        filtered_names.append(name)
        
        
    if pr == 'nan':
        pr = '------'
        filtered_pNumbers.append(pr)
        
    else:
        filtered_pNumbers.append(pr)
        
    if m_age == 'nan':
        m_age = '------'
        filtered_age.append(m_age)
        
    else:
        filtered_age.append(m_age)
        
    if m_love == 'nan':
        m_love = '------'
        filtered_love.append(m_love)
        
    else:
        filtered_love.append(m_love)
        
    if m_python == 'nan':
        m_python = '------'
        filtered_python.append(m_python)
        
    else:
        filtered_python.append(pr)            
def runner():
    show_table(filtered_names, filtered_pNumbers, filtered_age, filtered_love, filtered_python)
runner()
#print df.iloc[0]

#print df['Name']




# Splitting the dataset into the Training set and Test set
#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
