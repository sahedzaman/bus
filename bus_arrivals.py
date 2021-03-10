import requests

url = "https://transportapi.com/v3/uk/bus/stop/490008660N/live.json?app_id=9c400ecf&app_key=8624ad12adcb96619da049d0bcedece0&group=no&limit=2&nextbuses=yes"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)


bus_information = response.json() 

bus_time_one = (bus_information['departures']['all'])[0]['best_departure_estimate'] 
bus_time_two = (bus_information['departures']['all'])[1]['best_departure_estimate']


bus_number_one = (bus_information['departures']['all'])[0]['line'] 
bus_number_two = (bus_information['departures']['all'])[1]['line'] 

print(bus_number_one, bus_time_one)
print(bus_number_two, bus_time_two)

bus_stop_dic = { 'bus_number_one': 'bus_time_one'}

