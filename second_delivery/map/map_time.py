import folium
from folium import plugins
import os
import pandas as pd


data = pd.read_csv('../datasets/longitudeFixed.csv')

m = folium.Map(location=[25, 24], zoom_start=3,)
folium.TileLayer('openstreetmap').add_to(m)
folium.TileLayer('Stamen Terrain').add_to(m)
folium.LayerControl(collapsed=False).add_to(m)

plugins.Fullscreen(
    position='topright',
    title='Expand me',
    title_cancel='Exit me',
    force_separate_button=True
).add_to(m)

minimap = plugins.MiniMap()
m.add_child(minimap)

points = []

for index, row in data.iterrows():
    time = row['date']
    latitude = row['latitude']
    longitude = row['longitude']
    popup = '<p>' + str(time) + '</p>'
    coordinates = [longitude, latitude]
    
    if str(time) != 'nan':
        points.append({
                'time': time,
                'popup': popup,
                'coordinates': coordinates
            })
    
#print(points)

features = [
    {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': point['coordinates'],
        },
        'properties': {
            'time': point['time'],
            'popup': point['popup'],
            'id': 'house',
            'icon': 'circle',
            'iconstyle': {
                'fillColor': 'red',
                'fillOpacity': 0.6,
                'stroke': 'false',
                'radius': 6
            }
        }
    } for point in points
]

plugins.TimestampedGeoJson(
    {
        'type': 'FeatureCollection',
        'features': features
    },
    period='P1M',
    add_last_point=True,
    auto_play=False,
    loop=False,
    max_speed=1,
    loop_button=True,
    date_options='YYYY/MM/DD',
    time_slider_drag_update=True,
    duration='P2M'
).add_to(m)

m.save('html_files/map_time.html')
