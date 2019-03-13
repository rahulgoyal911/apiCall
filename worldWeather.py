import requests
key = "4dddafc191664c47ab1140145191203"
loc = str(30.723)+","+str(76.789)
url = "https://api.worldweatheronline.com/premium/v1/weather.ashx"+"?q="+loc+"&key="+key+"&format=json"

response = requests.get(url)
response = response.content.decode("utf-8")
print(response)
# print(url)