import pandas as pd

def get_fips_state(state,fips_file):
    for index, row in fips_file.iterrows():
        if state==row['Name']:
            return row['State (FIPS)']

def generate_dictionary(file):
    dictionary = { "cairo city" : "12400" }
    for index, row in file.iterrows():
        city_name = str(row['Area Name']).lower()
        if "city" in city_name:
            if "city city" in city_name:
                city_name = city_name.replace("city ", "")
            dictionary[city_name] = row['Place Code (FIPS)']
    return dictionary

our_data = pd.read_csv('longitudeFixed.csv', sep=',')
fips_f1 = pd.read_csv('state-geocodes-v2016.csv', sep=',')
fips_f2 = pd.read_csv('all-geocodes-v2016.csv', sep=',')

print('----------State codes:----------')

for index, row in our_data.iterrows():
    state = row['provstate']
    fips = get_fips_state(state,fips_f1)
    print(fips)

dictionary_of_fips = generate_dictionary(fips_f2)

print('----------City codes:----------')

for index, row in our_data.iterrows():
    city = row['city']
    city = str(city).lower()
    if not "city" in city:
        city = city + " city"
    if city in dictionary_of_fips:
        fips = dictionary_of_fips[city]
    else:
        fips = "None"
    print(fips)
