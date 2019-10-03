import pandas as pd 
import folium
from folium.plugins import HeatMap
from folium import FeatureGroup, LayerControl, Map, Marker

data = pd.read_csv('../../primera_entrega/datasets/preprocessed_dataset.csv')

data_republican = data[data['president_party'] == 'Republican']
data_democratic = data[data['president_party'] == 'Democratic']
latitude_longitude_republican = data_republican[['latitude','longitude']]
latitude_longitude_democratic = data_democratic[['latitude','longitude']]

hmap = folium.Map(location=[25, 24], zoom_start=3, )

democratic = FeatureGroup(name='Democratic')
republican = FeatureGroup(name='Republican')

HeatMap( data = latitude_longitude_republican,
                   min_opacity=0.2,
                   radius=6, blur=2,
                   gradient={.4: 'lime', .65: 'lime', 1: 'blue'},
                   max_zoom=1, 
                   layers='republican',
                   overlay=False
                 ).add_to(republican)
HeatMap( data = latitude_longitude_democratic,
                   min_opacity=0.2,
                   radius=6, blur=2, 
                   gradient={.4: 'lime', .65: 'lime', 1: 'red'},
                   max_zoom=1,
                   layers='democratic',
                   overlay=False
                 ).add_to(democratic)

m = Map(
    location=[25, 24],
    zoom_start=3,
    tiles='Stamen Terrain'
)
democratic.add_to(m)
republican.add_to(m)
LayerControl().add_to(m)
m.save('heatmap.html')
