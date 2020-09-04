import requests

response = requests.get("https://api.exchangerateapi.io/latest?symbols=USD")
print (response.text)
