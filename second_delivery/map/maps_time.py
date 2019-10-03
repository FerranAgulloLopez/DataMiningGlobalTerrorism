import folium
from folium import plugins
import os
import pandas as pd

table = """\
<table style=\'width:100%\'>
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td>
    <td>94</td>
  </tr>
</table>
"""

data = pd.read_csv('../../primera_entrega/datasets/preprocessed_dataset.csv')

points = []

for index, row in data.iterrows():
    
    #time_old = row['date'].split('-')
    #month = time_old[0]
    #day = time_old[1]
    #year = time_old[2]
    time = row['date']
    latitude = row['latitude']
    longitude = row['longitude']
    
    #time_new = year + '-' + month + '-' + day
    popup = '<p>' + str(time) + '</p>'
    coordinates = [longitude, latitude]
    
    points.append({
            'time': time,
            'popup': popup,
            'coordinates': coordinates
        })

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
            'icon': 'marker',
            'iconstyle': {
                'iconUrl': 'https://cdn1.iconfinder.com/data/icons/unigrid-military/60/002_military_battle_attack_swords-512.png',
                'iconSize': [20, 20]
            }
        }
    } for point in points
]

features.append(
    {
        'type': 'Feature',
        'geometry': {
            'type': 'LineString',
            'coordinates': [
                [-2.548828, 51.467697],
                [-0.087891, 51.536086],
                [-6.240234, 53.383328],
                [-1.40625, 60.261617],
                [-1.516113, 53.800651]
            ],
        },
        'properties': {
            'popup': 'Current address',
            'times': [
                '2017-06-02',
                '2017-07-02',
                '2017-08-02',
                '2017-09-02',
                '2017-10-02'
            ],
            'icon': 'circle',
            'iconstyle': {
                'fillColor': 'green',
                'fillOpacity': 0.6,
                'stroke': 'false',
                'radius': 13
            },
            'style': {'weight': 0},
            'id': 'man'
        }
    }
)

m = folium.Map(
    location=[25, 24],
    tiles='cartodbpositron',
    zoom_start=3,
)

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

m.save('heatmap_time.html')
