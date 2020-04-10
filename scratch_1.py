import pandas as pd

df = pd.read_csv('/Users/kitaeklee/PycharmProjects/DataVis_Police/Police_Department_Incidents_-_Previous_Year__2016_.csv')

df = df.loc[:, ['PdDistrict', 'Resolution']]
df = df.drop()
