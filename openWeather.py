import requests
key = "29d82cbfe71ac2746d1af20dffd66b23"
url = "http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID="+key;

response = requests.get(url)
response = response.content.decode("utf-8")
print(response)
# print(url)