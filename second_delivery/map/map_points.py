import pandas as pd 
import folium
from folium.plugins import HeatMap
from folium import FeatureGroup, LayerControl, Map, Marker, plugins
import os

# GENERAL CONFIG

data = pd.read_csv('../datasets/longitudeFixed.csv')

m = folium.Map(location=[25, 24], zoom_start=3,)
folium.TileLayer('openstreetmap').add_to(m)
folium.TileLayer('Stamen Terrain').add_to(m)

plugins.Fullscreen(
    position='topright',
    title='Expand me',
    title_cancel='Exit me',
    force_separate_button=True
).add_to(m)

minimap = plugins.MiniMap()
m.add_child(minimap)


# 1rst SECTION --> all attacks (heatmap)

all_attacks_layer = FeatureGroup(name='All attacks', overlay=True, control=True, show=True)

data_republican = data[data['president_party'] == 'Republican']
data_democratic = data[data['president_party'] == 'Democratic']
latitude_longitude_republican = data_republican[['latitude','longitude']]
latitude_longitude_democratic = data_democratic[['latitude','longitude']]

HeatMap( data = data[['latitude','longitude']],
                   min_opacity=0.2,
                   radius=6, blur=2,
                   gradient={.4: 'lime', .65: 'lime', 1: 'green'},
                   max_zoom=1, 
                   layers='republican',
                   overlay=False
                 ).add_to(all_attacks_layer)

m.add_child(all_attacks_layer)


# 2nd SECTION --> president_party (heatmap)

president_party_layer = FeatureGroup(name='President party', overlay=True, control=True, show=False)
republican_layer = plugins.FeatureGroupSubGroup(president_party_layer, '_____ Republican', overlay=True, control=True, show=True)
democratic_layer = plugins.FeatureGroupSubGroup(president_party_layer, '_____ Democratic', overlay=True, control=True, show=True)

data_republican = data[data['president_party'] == 'Republican']
data_democratic = data[data['president_party'] == 'Democratic']
latitude_longitude_republican = data_republican[['latitude','longitude']]
latitude_longitude_democratic = data_democratic[['latitude','longitude']]

HeatMap( data = latitude_longitude_republican,
                   min_opacity=0.2,
                   radius=6, blur=2,
                   gradient={.4: 'lime', .65: 'lime', 1: 'blue'},
                   max_zoom=1, 
                   layers='republican',
                   overlay=False
                 ).add_to(republican_layer)
HeatMap( data = latitude_longitude_democratic,
                   min_opacity=0.2,
                   radius=6, blur=2, 
                   gradient={.4: 'lime', .65: 'lime', 1: 'red'},
                   max_zoom=1,
                   layers='democratic',
                   overlay=False
                 ).add_to(democratic_layer)

m.add_child(president_party_layer)
m.add_child(republican_layer)
m.add_child(democratic_layer)


# SAVE MAP

folium.LayerControl(collapsed=False).add_to(m)
m.save('html_files/map_points.html')
