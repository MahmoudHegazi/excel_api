# excel_api

##test it
```python
import pandas as pd
nx = pd.read_excel('summary of results for research.xlsx')
print(nx['BRANCH_NAME'].apply(lambda x: x))
def branch_name(x):
    return x 
print(nx[['BRANCH_NAME','CLIENT_AREA']].apply(branch_name))
for row in nx.itertuples(index=True, name='Pandas'):
    print(row.BRANCH_ID, row.BRANCH_NAME)
for index, values in  nx.iterrows():
    BRANCH_ID, BRANCH_NAME, LOAN_ID,CLIENT_NAME,LAST_DUE_DATE,NO_OF_LOAN = values
    print(BRANCH_NAME,NO_OF_LOAN)
for i in range(len(nx)):
    print(nx.loc[i].BRANCH_NAME)
for i in range(nx.shape[0]):
    print(nx.loc[i].BRANCH_NAME)
```    
