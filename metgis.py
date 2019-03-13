import requests 
# Make a get request to get the latest position of the international space station from the opennotify api.
key = "mD0yVm1yvZ8fdK3dibaZKprTz1rqNm13QECG2j40W4UgMaLB8"
lat = 30.7239
lon = 76.7896
alt = 1000
ver = "sum3"
url = "https://api.metgis.com/forecast?key="+key+"&lat="+(str)(lat)+"&lon="+(str)(lon)+"&alt="+(str)(alt)+"&v="+ver+"&lang=en"
response = requests.get(url)

snowfall = response.json().get('snowfall')
windspeed = response.json().get('windSpeed')
windDirection = response.json().get('windDir')
rainfall = response.json().get('rainfall')
relativeHumidity = response.json().get('relativeHumidity')

print(snowfall)
print(windspeed)
print(windDirection)
print(rainfall)
print(relativeHumidity)

# print(response.headers)