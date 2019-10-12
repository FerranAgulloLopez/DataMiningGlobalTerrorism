import branca
import json
import folium
import requests
import pandas as pd

total_warns = 0


data = pd.read_csv('../datasets/fips-codes-added.csv')
url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
county_geo = f'{url}/us_counties_20m_topo.json'

colorscale = branca.colormap.linear.YlOrRd_09.scale(0, 100)

dict_fips = {}
for index, row in data.iterrows():
     fip = str(row['city_fips']).replace('.0','')
     if fip != 'nan':
        if fip in dict_fips:
            num = dict_fips[fip]
            dict_fips[fip] = num + 1
        else:
            dict_fips[fip] = 1

print(dict_fips)

def style_function(feature):
    global total_warns
    fip = feature['id'][-5:]
    color = 'white'
    if fip in dict_fips:
        count = dict_fips[fip]
        color = colorscale(count)
    else:
        total_warns += 1
    return {
        'fillOpacity': 0.5,
        'weight': 0,
        'fillColor': color
    }


m = folium.Map(
    location=[48, -102],
    tiles='cartodbpositron',
    zoom_start=3
)

folium.TopoJson(
    json.loads(requests.get(county_geo).text),
    'objects.us_counties_20m',
    style_function=style_function
).add_to(m)

m.save('html_files/map_provs.html')
print('Total empty fips: ' + str(total_warns))
