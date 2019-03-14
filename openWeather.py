import requests
key = "29d82cbfe71ac2746d1af20dffd66b23"
url = "http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID="+key;

response = requests.get(url)
# response = response.content.decode("utf-8")
# print(response)

cod = response.json().get("cod")
message = response.json().get("message")
count = response.json().get("cnt")

# print(count)
for x in range(0,count):
    dt = response.json().get("list")[x].get("dt")

    temp = response.json().get("list")[x].get('main').get("temp")
    temp_min = response.json().get("list")[x].get('main').get("temp_min")
    temp_max = response.json().get("list")[x].get('main').get("temp_max")
    pressure = response.json().get("list")[x].get('main').get("pressure")
    sea_level = response.json().get("list")[x].get('main').get("sea_level")
    grnd_level = response.json().get("list")[x].get('main').get("grnd_level")
    humidity = response.json().get("list")[x].get('main').get("humidity")
    temp_kf = response.json().get("list")[x].get('main').get("temp_kf")

    weather_id = response.json().get("list")[x].get('weather')[0].get("id")
    weather_main = response.json().get("list")[x].get('weather')[0].get("main")
    weather_desc = response.json().get("list")[x].get('weather')[0].get("description")
    weather_icon = response.json().get("list")[x].get('weather')[0].get("icon")

    clouds_all = response.json().get("list")[x].get('clouds').get("all")

    wind_speed = response.json().get("list")[x].get('wind').get("speed")
    wid_deg = response.json().get("list")[x].get('wind').get("deg")

    snow = response.json().get("list")[x].get('snow')

    sys_pod = response.json().get("list")[x].get('sys').get('pod')

    dt_text = response.json().get("list")[x].get('dt_text')

    city_id = response.json().get("city").get('id')
    city_name = response.json().get("city").get('name')
    city_coord_lat = response.json().get("city").get('coord').get('lat')
    city_coord_lon = response.json().get("city").get('coord').get('lon')
    city_coord_country = response.json().get("city").get('country')

    print(temp)

# print(url)