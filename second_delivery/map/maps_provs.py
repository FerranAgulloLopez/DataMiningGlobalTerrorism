import branca
import json
import folium
import requests
import pandas as pd

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

total_warns = 0
total_ok = 0

data = pd.read_csv('../datasets/fips-codes-added.csv')
url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
county_geo = f'{url}/us_counties_20m_topo.json'

colorscale = branca.colormap.linear.YlOrRd_09.scale(0, 20)

dict_fips = {}
for index, row in data.iterrows():
     fip = str(row['city_fips']).replace('.0','')
     if fip != 'nan':
        if fip in dict_fips:
            num = dict_fips[fip]
            dict_fips[fip] = num + 1
        else:
            dict_fips[fip] = 1

strange_dict = dict_fips

def style_function(feature):
    global total_warns, total_ok, strange_dict, dict_fips
    fip = feature['id'][-5:]
    count = 0
    if fip in dict_fips:
        count = dict_fips[fip]
        total_ok += 1
        strange_dict = removekey(strange_dict,fip)
    else:
        total_warns += 1
    return {
        'fillOpacity': 0.5,
        'weight': 0,
        'fillColor': colorscale(count)
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
print('empty fips: ' + str(total_warns) + '; ok fips: ' + str(total_ok))
print('unknown fips: ' + str(len(strange_dict)) + '; total fips: ' + str(len(dict_fips)))
