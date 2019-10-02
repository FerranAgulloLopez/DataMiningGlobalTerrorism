import pandas as pd 
import folium
from folium.plugins import HeatMap

data = pd.read_csv('../../first_delivery/datasets/preprocessed_dataset.csv')

data_republican = data[data['president_party'] == 'Republican']
data_democratic = data[data['president_party'] == 'Democratic']
latitude_longitude_republican = data_republican[['latitude','longitude']]
latitude_longitude_democratic = data_democratic[['latitude','longitude']]

hmap = folium.Map(location=[25, 24], zoom_start=3, )

hm_wide = HeatMap( data = latitude_longitude_republican,
                   min_opacity=0.2,
                   radius=6, blur=2,
                   gradient={.4: 'lime', .65: 'lime', 1: 'blue'},
                   max_zoom=1, 
                 )
hm_wide2 = HeatMap( data = latitude_longitude_democratic,
                   min_opacity=0.2,
                   radius=6, blur=2, 
                   gradient={.4: 'lime', .65: 'lime', 1: 'red'},
                   max_zoom=1, 
                 )
hmap.add_child(hm_wide)
hmap.add_child(hm_wide2)
hmap.save('heatmap.html')
