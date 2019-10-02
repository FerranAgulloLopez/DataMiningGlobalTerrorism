import pandas as pd
import folium
import os
 
state_geo = os.path.join('.', 'us-states.json') # https://github.com/python-visualization/folium/blob/master/tests/us-states.json

dataset = pd.read_csv('../../first_delivery/datasets/preprocessed_dataset.csv')

m = folium.Map(location=[25, 24], zoom_start=3, )

dict_states = {}
for index, row in dataset.iterrows():
     state = row['provstate']
     if state in dict_states:
        num = dict_states[state]
        dict_states[state] = num + 1
     else:
        dict_states[state] = 1

array = []
array.append(['AZ',40])
for state, count in dict_states.items():
    array.append([state,count])
data_states_num_attacks = pd.DataFrame(array, columns = ['state', 'count'])

print(data_states_num_attacks)

folium.Choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=data_states_num_attacks,
    columns=['state', 'count'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Number of attacks'
).add_to(m)

folium.LayerControl().add_to(m)
 
# Save to html
m.save('heatmap_states.html')
