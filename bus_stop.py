import requests 

response = requests.get("https://api.postcodes.io/postcodes/NW51TL")

print(response.json())


print (response.json()["result"]["longitude"])
print (response.json()["result"]["latitude"])

data_one = {'longitude':-0.144754, 'latitude':51.553935}
response_one = requests.get("http://transportapi.com/v3/uk/places.json?type=bus_stop",params=data_one)
print (response_one)



