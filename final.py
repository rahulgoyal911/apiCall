import threading 
import time
import requests

def metgis(arg):
    while(arg):
        key = "mD0yVm1yvZ8fdK3dibaZKprTz1rqNm13QECG2j40W4UgMaLB8"
        lat = 30.7239
        lon = 76.7896
        alt = 1000
        ver = "sum3"
        url = "https://api.metgis.com/forecast?key="+key+"&lat="+(str)(lat)+"&lon="+(str)(lon)+"&alt="+(str)(alt)+"&v="+ver+"&lang=en"
        response = requests.get(url)
        sunrise = response.json().get('sunrise')
        dayCount = response.json().get('dayCount')
        weatherIcon = response.json().get('weatherIcon')
        snowfall = response.json().get('snowfall')
        unitLin = response.json().get('unitLin')
        maxTemp = response.json().get('maxTemp')
        description = response.json().get('description')
        dateRequest = response.json().get('dateRequest')
        windDir = response.json().get('windDir')
        sunshineDuration = response.json().get('sumshineDuration')
        precipitaton = response.json().get('precipitation')
        windIcon = response.json().get('windIcon')
        windSpeed = response.json().get('windSpeed')
        lang = response.json().get('lang')
        rainfall = response.json().get('rainfall')
        unitWind = response.json().get('unitWind')
        alt = response.json().get('alt')
        forecastIssued = response.json().get('forecastIssued')
        minTemp = response.json().get('minTemp')
        unitTemp = response.json().get('unitTemp')
        sunset = response.json().get('sunset')
        relativeHumidity = response.json().get('relativeHumidity')
        forecastShortText = response.json().get('forecastShortText')
        print(sunrise)
        print(dayCount)
        print(weatherIcon)
        print(snowfall)
        print(unitLin)
        print(maxTemp)
        print(description)
        print(dateRequest)
        print(windDir)
        print(sunshineDuration)
        print(precipitaton)
        print(windIcon)
        print(windSpeed)
        print(lang)
        print(rainfall)
        print(unitWind)
        print(alt)
        print(forecastIssued)
        print(minTemp)
        print(unitTemp)
        print(sunset)
        print(relativeHumidity)
        print(forecastShortText)
        time.sleep(1)
        # arg=0


# metgis function till here

def openWeather(arg):
    while(arg):
        key = "29d82cbfe71ac2746d1af20dffd66b23"
        lat = str(30.723)
        lon = str(76.789)
        url = "http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID="+key
        url = "http://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&APPID="+key
        response = requests.get(url)
        id1 = response.json().get("weather")[0].get("id")
        main = response.json().get("weather")[0].get("main")
        description = response.json().get("weather")[0].get("description")
        icon = response.json().get("weather")[0].get("icon")
        icon = response.json().get("main").get("temp")
        pressure = response.json().get("main").get("pressure")
        humidity = response.json().get("main").get("humidity")
        temp_min = response.json().get("main").get("temp_min")
        temp_max = response.json().get("main").get("temp_max")
        visibility = response.json().get("visibility")
        speed = response.json().get("wind").get("speed")
        deg = response.json().get("wind").get("deg")
        clouds = response.json().get("clouds").get("all")
        dt = response.json().get("dt")
        typ = response.json().get("sys").get("type")
        id = response.json().get("sys").get("id")
        message = response.json().get("sys").get("message")
        country = response.json().get("sys").get("country")
        sunrise = response.json().get("sys").get("sunrise")
        sunset = response.json().get("sys").get("sunset")
        idn = response.json().get("id")
        name = response.json().get("name")
        print(id1)
        print(main)
        print(description)
        print(icon)
        print(icon)
        print(pressure)
        print(humidity)
        print(temp_min)
        print(temp_max)
        print(visibility)
        print(speed)
        print(deg)
        print(clouds)
        print(dt)
        print(typ)
        print(id)
        print(message)
        print(country)
        print(sunrise)
        print(sunset)
        print(idn)
        print(name)
        time.sleep(1)
        # arg=0

# open weather till here

def worldWeather(arg):
    while(arg):
        key = "4dddafc191664c47ab1140145191203"
        lat = 30.723
        lon = 76.789
        loc = str(lat)+","+str(lon)
        url = "https://api.worldweatheronline.com/premium/v1/weather.ashx"+"?q="+loc+"&key="+key+"&format=json"
        response = requests.get(url)
        # response = response.content.decode("utf-8")
        types = response.json().get("data").get("request")[0].get("type")
        querys = response.json().get("data").get("request")[0].get("query")
        observation_time = response.json().get("data").get("current_condition")[0].get("observation_time")
        temp_C = response.json().get("data").get("current_condition")[0].get("temp_C")
        temp_F = response.json().get("data").get("current_condition")[0].get("temp_F")
        weatherCode = response.json().get("data").get("current_condition")[0].get("weatherCode")
        weatherIconUrl = response.json().get("data").get("current_condition")[0].get("weatherIconUrl")[0].get("value")
        weatherDesc = response.json().get("data").get("current_condition")[0].get("weatherDesc")[0].get("value")
        windSpeedMiles = response.json().get("data").get("current_condition")[0].get("windSpeedMiles")
        windSpeedKmph = response.json().get("data").get("current_condition")[0].get("windSpeedKmph")
        winddirDegree = response.json().get("data").get("current_condition")[0].get("winddirDegree")
        winddir16Point = response.json().get("data").get("current_condition")[0].get("winddir16Point")
        precipMM = response.json().get("data").get("current_condition")[0].get("precipMM")
        humidity = response.json().get("data").get("current_condition")[0].get("humidity")
        visibility = response.json().get("data").get("current_condition")[0].get("visibility")
        pressure = response.json().get("data").get("current_condition")[0].get("pressure")
        cloudcover = response.json().get("data").get("current_condition")[0].get("cloudcover")
        FeelsLikeC = response.json().get("data").get("current_condition")[0].get("FeelsLikeC")
        FeelsLikeF = response.json().get("data").get("current_condition")[0].get("FeelsLikeF")
        uvIndex = response.json().get("data").get("current_condition")[0].get("uvIndex")
        # 0,14
        for day in range(0,1):
            date = response.json().get("data").get("weather")[day].get("date")
            sunrise = response.json().get("data").get("weather")[day].get("astronomy")[0].get("sunrise")
            sunset = response.json().get("data").get("weather")[day].get("astronomy")[0].get("sunset")
            moonrise = response.json().get("data").get("weather")[day].get("astronomy")[0].get("moonrise")
            moonset = response.json().get("data").get("weather")[day].get("astronomy")[0].get("moonset")
            moon_phase = response.json().get("data").get("weather")[day].get("astronomy")[0].get("moon_phase")
            moon_illumination = response.json().get("data").get("weather")[day].get("astronomy")[0].get("moon_illumination")
            maxtempC = response.json().get("data").get("weather")[day].get("maxtempC")
            maxtempF = response.json().get("data").get("weather")[day].get("maxtempF")
            mintempC = response.json().get("data").get("weather")[day].get("mintempC")
            mintempF = response.json().get("data").get("weather")[day].get("mintempF")
            totalSnow_cm = response.json().get("data").get("weather")[day].get("totalSnow_cm")
            sunHour = response.json().get("data").get("weather")[day].get("sunHour")
            uvIndex = response.json().get("data").get("weather")[day].get("uvIndex")
        # 0,8
            for hour in range (0,1):
                times = response.json().get("data").get("weather")[day].get("hourly")[hour].get("time")
                tempC = response.json().get("data").get("weather")[day].get("hourly")[hour].get("tempC")
                tempF = response.json().get("data").get("weather")[day].get("hourly")[hour].get("tempF")
                windspeedMiles = response.json().get("data").get("weather")[day].get("hourly")[hour].get("windspeedMiles")
                windspeedkmph = response.json().get("data").get("weather")[day].get("hourly")[hour].get("windspeedkmph")
                winddirDegree = response.json().get("data").get("weather")[day].get("hourly")[hour].get("winddirDegree")
                weatherCode = response.json().get("data").get("weather")[day].get("hourly")[hour].get("weatherCode")
                winddir16Point = response.json().get("data").get("weather")[day].get("hourly")[hour].get("winddir16Point")
                weatherIconUrl = response.json().get("data").get("weather")[day].get("hourly")[hour].get("weatherIconUrl")[0].get("value")
                weatherDesc = response.json().get("data").get("weather")[day].get("hourly")[hour].get("weatherDesc")[0].get("value")
                precipMM = response.json().get("data").get("weather")[day].get("hourly")[hour].get("precipMM")
                humidity = response.json().get("data").get("weather")[day].get("hourly")[hour].get("humidity")
                visibility = response.json().get("data").get("weather")[day].get("hourly")[hour].get("visibility")
                pressure = response.json().get("data").get("weather")[day].get("hourly")[hour].get("pressure")
                cloudcover = response.json().get("data").get("weather")[day].get("hourly")[hour].get("cloudcover")
                HeatIndexC = response.json().get("data").get("weather")[day].get("hourly")[hour].get("HeatIndexC")
                HeatIndexF = response.json().get("data").get("weather")[day].get("hourly")[hour].get("HeatIndexF")
                DewPointC = response.json().get("data").get("weather")[day].get("hourly")[hour].get("DewPointC")
                DewPointF = response.json().get("data").get("weather")[day].get("hourly")[hour].get("DewPointF")
                WindChillC = response.json().get("data").get("weather")[day].get("hourly")[hour].get("WindChillC")
                WindChillF = response.json().get("data").get("weather")[day].get("hourly")[hour].get("WindChillF")
                WindGustMiles = response.json().get("data").get("weather")[day].get("hourly")[hour].get("WindGustMiles")
                WindGustKmph = response.json().get("data").get("weather")[day].get("hourly")[hour].get("WindGustKmph")
                FeelsLikeC = response.json().get("data").get("weather")[day].get("hourly")[hour].get("FeelsLikeC")
                FeelsLikeF = response.json().get("data").get("weather")[day].get("hourly")[hour].get("FeelsLikeF")
                chanceofrain = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceofrain")
                chanceofremdry = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceofremdry")
                chanceofwindy = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceofwindy")
                chanceofovercast = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceofovercast")
                chanceofsunshine = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceofsunshine")
                chanceoffrost = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceoffrost")
                chanceofhightemp = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceofhightemp")
                chanceoffog = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceoffog")
                chanceofsnow = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceofsnow")
                chanceofthunder = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceofthunder")
                uvIndex = response.json().get("data").get("weather")[day].get("hourly")[hour].get("uvIndex")
        # 0,12
        # climate averages
        for month in range(0,1):
            index = response.json().get("data").get("ClimateAverages")[0].get("month")[month].get("index")
            name = response.json().get("data").get("ClimateAverages")[0].get("month")[month].get("name")
            avgMinTemp = response.json().get("data").get("ClimateAverages")[0].get("month")[month].get("avgMinTemp")
            avgMinTemp_F = response.json().get("data").get("ClimateAverages")[0].get("month")[month].get("avgMinTemp_F")
            absMaxTemp = response.json().get("data").get("ClimateAverages")[0].get("month")[month].get("absMaxTemp")
            absMaxTemp_F = response.json().get("data").get("ClimateAverages")[0].get("month")[month].get("absMaxTemp_F")
            avgDailyRainfall = response.json().get("data").get("ClimateAverages")[0].get("month")[month].get("avgDailyRainfall")
        # print(url)
        print(types)
        print(querys)
        print(observation_time)
        print(temp_C)
        print(temp_F)
        print(weatherCode)
        print(weatherIconUrl)
        print(weatherDesc)
        print(windSpeedMiles)
        print(windSpeedKmph)
        print(winddirDegree)
        print(winddir16Point)
        print(precipMM)
        print(humidity)
        print(visibility)
        print(pressure)
        print(cloudcover)
        print(FeelsLikeC)
        print(FeelsLikeF)
        print(uvIndex)
        print(date)
        print(sunrise)
        print(sunset)
        print(moonrise)
        print(moonset)
        print(moon_phase)
        print(moon_illumination)
        print(maxtempC)
        print(maxtempF)
        print(mintempC)
        print(mintempF)
        print(totalSnow_cm)
        print(sunHour)
        print(uvIndex)
        print(times)
        print(tempC)
        print(tempF)
        print(windspeedMiles)
        print(windspeedkmph)
        print(winddirDegree)
        print(weatherCode)
        print(winddir16Point)
        print(weatherIconUrl)
        print(weatherDesc)
        print(precipMM)
        print(humidity)
        print(visibility)
        print(pressure)
        print(cloudcover)
        print(HeatIndexC)
        print(HeatIndexF)
        print(DewPointC)
        print(DewPointF)
        print(WindChillC)
        print(WindChillF)
        print(WindGustMiles)
        print(WindGustKmph)
        print(FeelsLikeC)
        print(FeelsLikeF)
        print(chanceofrain)
        print(chanceofremdry)
        print(chanceofwindy)
        print(chanceofovercast)
        print(chanceofsunshine)
        print(chanceoffrost)
        print(chanceofhightemp)
        print(chanceoffog)
        print(chanceofsnow)
        print(chanceofthunder)
        print(uvIndex)
        time.sleep(1)
        # arg=0

# worldWeather till here

# main
t1 = threading.Thread(target=metgis, args=(1,)) 
t2 = threading.Thread(target=openWeather, args=(1,)) 
t3 = threading.Thread(target=worldWeather, args=(1,)) 

t1.start() 
t2.start() 
t3.start()

t1.join()
t2.join()
t3.join()
print("Done")
