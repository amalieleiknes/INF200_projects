import matplotlib.pyplot as plt
import pandas
import requests

endpoint = 'https://frost.met.no/observations/v0.jsonld'
parameters = {
    'sources': 'SN17850',
    'elements': 'mean(air_temperature P1D)',
    'referencetime': '2021-01-01/2021-09-26',
}

with open("../IDs", 'r') as IDfile:
    client_id = IDfile.read()

    frost_response = requests.get(endpoint, parameters, auth=(client_id, ' '))
    assert frost_response.status_code == 200


print(frost_response.url)

for header_name, header_value in frost_response.headers.items():
    print(f'{header_name:16s}: {header_value}')


frost_payload = frost_response.json()

type(frost_payload)
frost_payload['data'][:2]

temp_data = [{'Time': pandas.to_datetime(entry['referenceTime']),
              'T_avg': entry['observations'][0]['value']}
             for entry in frost_payload['data']]
temp_data[:4]


T_data = pandas.DataFrame.from_records(temp_data).set_index('Time')
print(T_data.head())

T_data.plot()

