import pandas as pd

def generate_dictionary_fips_city(file):
    dictionary = {}
    for index, row in file.iterrows():
        city_name = row['Name'].lower()
        dictionary[city_name] = row['FIPS']
    return dictionary

def generate_dictionary_fips_state(file):
    dictionary = {}
    for index, row in file.iterrows():
        state_name = row['Name'].lower()
        dictionary[state_name] = row['State (FIPS)']
    return dictionary

data = pd.read_csv('../datasets/longitudeFixed.csv', sep=',')
fips_city = pd.read_csv('../datasets/fips_codes_city.csv', sep=',')
fips_state = pd.read_csv('../datasets/fips_codes_state.csv', sep=',')

dictionary_fips_city = generate_dictionary_fips_city(fips_city)
dictionary_fips_state = generate_dictionary_fips_state(fips_state)

array_fips_city = []
array_fips_state = []

count__fips_city_inserted = 0
count__fips_state_inserted = 0

for index, row in data.iterrows():
    
    # city

    city = str(row['city']).lower()
    value = "NA"
    if city in dictionary_fips_city:
        value = dictionary_fips_city[city]
        count__fips_city_inserted += 1
    array_fips_city.append(value)
    
    # state
    state = str(row['provstate']).lower()
    value = "NA"
    if state in dictionary_fips_state:
        value = dictionary_fips_state[state]
        count__fips_state_inserted += 1
    array_fips_state.append(value)
    

data['city_fips'] = array_fips_city
data['state_fips'] = array_fips_state
total_rows = len(data.index)
print('city nans -> ' + str(100-(count__fips_city_inserted/total_rows)*100) + '% ; state nans -> ' + str(100-(count__fips_state_inserted/total_rows)*100) + ' %')
data.to_csv('../datasets/fips-codes-added.csv')
