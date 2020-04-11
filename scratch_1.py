import pandas as pd

df = pd.read_csv('/Users/kitaeklee/PycharmProjects/DataVis_Police/Police_Department_Incidents_-_Previous_Year__2016_.csv')

df = df.loc[:, ['PdDistrict', 'Category']]

# Get the names of indexes for the column 'Category' with the value 'NON-CRIMINAL'
index_names = df[df['Category'] == 'NON-CRIMINAL'].index
# Drop those rows
df.drop(index_names, inplace=True)
df.reset_index()

# Create new dataframe grouped by the District and allocate number of crimes occurred
df_new = df.groupby('PdDistrict').count()
df_new = df_new.reset_index()
df_new = df_new.rename(columns={'PdDistrict':'Neighborhood', 'Category':'Count'})

print(df_new)

import folium


sf_geo = r'/Users/kitaeklee/PycharmProjects/DataVis_Police/san-francisco.geojson'

# Initialize the map
world_map = folium.Map(location=[37, -122], zoom_start=12, tiles='OpenStreetMap')
# Choropleth map
world_map.choropleth(geo_data=sf_geo, data=df_new, columns=['Neighborhood', 'Count'],
                     key_on='feature.properties.DISTRICT', fill_color='YlOrRd',
                     fill_opacity=0.7, line_opacity=0.2,
                     legend_name='Crime Rate in San Francisco')
world_map




