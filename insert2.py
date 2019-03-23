import threading 
import time
import requests
import psycopg2
import csv


conn = psycopg2.connect(database = "postgres", user = "postgres", password = "namespace1", hostaddr="35.198.246.100", port = "5432")
print ('Opened database successfully')
cur = conn.cursor()
lat = str(30.739)
lon = str(30.796)
alt = str(1000)


def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def getCoor(arg):
        global lat
        global lon
        global alt
        templat=""
        templon=""
        tempalt=""
        temppos=""
        # while(arg):
        ifile  = open('loc1.csv', "r")
        reader = csv.reader(ifile)
        rownum = 0
        for row in reader:
                if(row[4]!='Altitude'):
                        tempalt = str(row[4])
                        temppos=str(row[3])
                        temploc = temppos.split(',')
                        # print(loc)
                        templat = float(temploc[0])
                        templon = float(temploc[1])
                        templat = truncate(templat,3)
                        templon = truncate(templon,3)
                        lat = str(templat)
                        lon = str(templon)
                        alt = str(tempalt)
                        print(lat)
                        print(lon)
                        print(alt)
                        print("location done")


                        key = "mD0yVm1yvZ8fdK3dibaZKprTz1rqNm13QECG2j40W4UgMaLB8"
                        # lat = 30.7239
                        # lon = 76.7896
                        # alt = 1000
                        ver = "sum3"
                        url = "https://api.metgis.com/forecast?key="+key+"&lat="+(str)(lat)+"&lon="+(str)(lon)+"&alt="+(str)(alt)+"&v="+ver+"&lang=en"
                        # print(url)
                        response = requests.get(url)
                        # print(response)
                        if(response.status_code==200):
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
                                forecastIssued = response.json().get('forecastIssued')
                                minTemp = response.json().get('minTemp')
                                unitTemp = response.json().get('unitTemp')
                                sunset = response.json().get('sunset')
                                relativeHumidity = response.json().get('relativeHumidity')
                                forecastShortText = response.json().get('forecastShortText')

                                str1 = "INSERT INTO METGIS (lat,lon,alt,sunrise,dayCount,weatherIcon,snowfall,unitLin,maxTemp,description,dateRequest,windDir,sunshineDuration,precipitaton,windIcon,windSpeed,lang,rainfall,unitWind,forecastIssued,minTemp,unitTemp,sunset,relativeHumidity,forecastShortText) VALUES('"+str(lat)+"','"+str(lon)+"','"+str(alt)+"','"+str(sunrise[0])+"','"+str(dayCount)+"','"+str(weatherIcon[0])+"','"+str(snowfall[0])+"','"+str(unitLin)+"','"+str(maxTemp[0])+"','"+str(description)+"','"+str(dateRequest)+"','"+str(windDir[0])+"','"+str(sunshineDuration)+"','"+str(precipitaton[0])+"','"+str(windIcon[0])+"','"+str(windSpeed[0])+"','"+str(lang)+"','"+str(rainfall[0])+"','"+str(unitWind)+"','"+str(forecastIssued)+"','"+str(minTemp[0])+"','"+str(unitTemp)+"','"+str(sunset[0])+"','"+str(relativeHumidity)+"','"+str(forecastShortText[0])+"');"         
                                # print(str1)
                                cur.execute(str1)
                                str1 = "INSERT INTO METGIS (lat,lon,alt,sunrise,dayCount,weatherIcon,snowfall,unitLin,maxTemp,description,dateRequest,windDir,sunshineDuration,precipitaton,windIcon,windSpeed,lang,rainfall,unitWind,forecastIssued,minTemp,unitTemp,sunset,relativeHumidity,forecastShortText) VALUES('"+str(lat)+"','"+str(lon)+"','"+str(alt)+"','"+str(sunrise[1])+"','"+str(dayCount)+"','"+str(weatherIcon[1])+"','"+str(snowfall[1])+"','"+str(unitLin)+"','"+str(maxTemp[1])+"','"+str(description)+"','"+str(dateRequest)+"','"+str(windDir[1])+"','"+str(sunshineDuration)+"','"+str(precipitaton[1])+"','"+str(windIcon[1])+"','"+str(windSpeed[1])+"','"+str(lang)+"','"+str(rainfall[1])+"','"+str(unitWind)+"','"+str(forecastIssued)+"','"+str(minTemp[1])+"','"+str(unitTemp)+"','"+str(sunset[1])+"','"+str(relativeHumidity)+"','"+str(forecastShortText[1])+"');"         
                                cur.execute(str1)
                                str1 = "INSERT INTO METGIS (lat,lon,alt,sunrise,dayCount,weatherIcon,snowfall,unitLin,maxTemp,description,dateRequest,windDir,sunshineDuration,precipitaton,windIcon,windSpeed,lang,rainfall,unitWind,forecastIssued,minTemp,unitTemp,sunset,relativeHumidity,forecastShortText) VALUES('"+str(lat)+"','"+str(lon)+"','"+str(alt)+"','"+str(sunrise[2])+"','"+str(dayCount)+"','"+str(weatherIcon[2])+"','"+str(snowfall[2])+"','"+str(unitLin)+"','"+str(maxTemp[2])+"','"+str(description)+"','"+str(dateRequest)+"','"+str(windDir[2])+"','"+str(sunshineDuration)+"','"+str(precipitaton[2])+"','"+str(windIcon[2])+"','"+str(windSpeed[2])+"','"+str(lang)+"','"+str(rainfall[2])+"','"+str(unitWind)+"','"+str(forecastIssued)+"','"+str(minTemp[2])+"','"+str(unitTemp)+"','"+str(sunset[2])+"','"+str(relativeHumidity)+"','"+str(forecastShortText[2])+"');"         
                                cur.execute(str1)
                                conn.commit()
                                print("inserted into metgis")
                        else:
                                print(response.status_code)

                        key = "29d82cbfe71ac2746d1af20dffd66b23"
                        # lat = str(30.723)
                        # lon = str(76.789)
                        url = "http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID="+key
                        url = "http://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&APPID="+key
                        response = requests.get(url)
                        id1 = response.json().get("weather")[0].get("id")
                        main = response.json().get("weather")[0].get("main")
                        description = response.json().get("weather")[0].get("description")
                        icon = response.json().get("weather")[0].get("icon")
                        temp = response.json().get("main").get("temp")
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
                        id2 = response.json().get("sys").get("id")
                        message = response.json().get("sys").get("message")
                        country = response.json().get("sys").get("country")
                        sunrise = response.json().get("sys").get("sunrise")
                        sunset = response.json().get("sys").get("sunset")
                        idn = response.json().get("id")
                        name = response.json().get("name")
                        response = str(response)
                        id1 = str(id1)
                        main = str(main)
                        description = str(description)
                        icon = str(icon)
                        temp = str(temp)
                        pressure = str(pressure)
                        humidity = str(humidity)
                        temp_min = str(temp_min)
                        temp_max = str(temp_max)
                        visibility = str(visibility)
                        speed = str(speed)
                        deg = str(deg)
                        clouds = str(clouds)
                        dt = str(dt)
                        typ = str(typ)
                        id2 = str(id2)
                        message = str(message)
                        country = str(country)
                        sunrise = str(sunrise)
                        sunset = str(sunset)
                        idn = str(idn)
                        name = str(name)
                        str1 = "INSERT INTO openWeather (lat,lon,id1,main,description,icon,temp,pressure,humidity,temp_min,temp_max,visibility,speed,deg,clouds,dt,typ,id2,message,country,sunrise,sunset,idn,name) values ('"+lat+"','"+lon+"','"+id1+"','"+main+"','"+description+"','"+icon+"','"+temp+"','"+pressure+"','"+humidity+"','"+temp_min+"','"+temp_max+"','"+visibility+"','"+speed+"','"+deg+"','"+clouds+"','"+dt+"','"+typ+"','"+id2+"','"+message+"','"+country+"','"+sunrise+"','"+sunset+"','"+idn+"','"+name+"');"
                        # print(str1)
                        cur.execute(str1)
                        conn.commit()
                        print("inserted into openweather")

                        key = "4dddafc191664c47ab1140145191203"
                        # lat = 30.723
                        # lon = 76.789
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
                        windSpeedMiles = response.json().get("data").get("current_condition")[0].get("windspeedMiles")
                        windSpeedKmph = response.json().get("data").get("current_condition")[0].get("windspeedKmph")
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
                                day_date = response.json().get("data").get("weather")[day].get("date")
                                day_sunrise = response.json().get("data").get("weather")[day].get("astronomy")[0].get("sunrise")
                                day_sunset = response.json().get("data").get("weather")[day].get("astronomy")[0].get("sunset")
                                day_moonrise = response.json().get("data").get("weather")[day].get("astronomy")[0].get("moonrise")
                                day_moonset = response.json().get("data").get("weather")[day].get("astronomy")[0].get("moonset")
                                day_moon_phase = response.json().get("data").get("weather")[day].get("astronomy")[0].get("moon_phase")
                                day_moon_illumination = response.json().get("data").get("weather")[day].get("astronomy")[0].get("moon_illumination")
                                day_maxtempC = response.json().get("data").get("weather")[day].get("maxtempC")
                                day_maxtempF = response.json().get("data").get("weather")[day].get("maxtempF")
                                day_mintempC = response.json().get("data").get("weather")[day].get("mintempC")
                                day_mintempF = response.json().get("data").get("weather")[day].get("mintempF")
                                day_totalSnow_cm = response.json().get("data").get("weather")[day].get("totalSnow_cm")
                                day_sunHour = response.json().get("data").get("weather")[day].get("sunHour")
                                day_uvIndex = response.json().get("data").get("weather")[day].get("uvIndex")
                                # 0,8
                                for hour in range (0,1):
                                        hour_times = response.json().get("data").get("weather")[day].get("hourly")[hour].get("time")
                                        hour_tempC = response.json().get("data").get("weather")[day].get("hourly")[hour].get("tempC")
                                        hour_tempF = response.json().get("data").get("weather")[day].get("hourly")[hour].get("tempF")
                                        hour_windspeedMiles = response.json().get("data").get("weather")[day].get("hourly")[hour].get("windspeedMiles")
                                        hour_windspeedkmph = response.json().get("data").get("weather")[day].get("hourly")[hour].get("windspeedKmph")
                                        hour_winddirDegree = response.json().get("data").get("weather")[day].get("hourly")[hour].get("winddirDegree")
                                        hour_weatherCode = response.json().get("data").get("weather")[day].get("hourly")[hour].get("weatherCode")
                                        hour_winddir16Point = response.json().get("data").get("weather")[day].get("hourly")[hour].get("winddir16Point")
                                        hour_weatherIconUrl = response.json().get("data").get("weather")[day].get("hourly")[hour].get("weatherIconUrl")[0].get("value")
                                        hour_weatherDesc = response.json().get("data").get("weather")[day].get("hourly")[hour].get("weatherDesc")[0].get("value")
                                        hour_precipMM = response.json().get("data").get("weather")[day].get("hourly")[hour].get("precipMM")
                                        hour_humidity = response.json().get("data").get("weather")[day].get("hourly")[hour].get("humidity")
                                        hour_visibility = response.json().get("data").get("weather")[day].get("hourly")[hour].get("visibility")
                                        hour_pressure = response.json().get("data").get("weather")[day].get("hourly")[hour].get("pressure")
                                        hour_cloudcover = response.json().get("data").get("weather")[day].get("hourly")[hour].get("cloudcover")
                                        hour_HeatIndexC = response.json().get("data").get("weather")[day].get("hourly")[hour].get("HeatIndexC")
                                        hour_HeatIndexF = response.json().get("data").get("weather")[day].get("hourly")[hour].get("HeatIndexF")
                                        hour_DewPointC = response.json().get("data").get("weather")[day].get("hourly")[hour].get("DewPointC")
                                        hour_DewPointF = response.json().get("data").get("weather")[day].get("hourly")[hour].get("DewPointF")
                                        hour_WindChillC = response.json().get("data").get("weather")[day].get("hourly")[hour].get("WindChillC")
                                        hour_WindChillF = response.json().get("data").get("weather")[day].get("hourly")[hour].get("WindChillF")
                                        hour_WindGustMiles = response.json().get("data").get("weather")[day].get("hourly")[hour].get("WindGustMiles")
                                        hour_WindGustKmph = response.json().get("data").get("weather")[day].get("hourly")[hour].get("WindGustKmph")
                                        hour_FeelsLikeC = response.json().get("data").get("weather")[day].get("hourly")[hour].get("FeelsLikeC")
                                        hour_FeelsLikeF = response.json().get("data").get("weather")[day].get("hourly")[hour].get("FeelsLikeF")
                                        hour_chanceofrain = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceofrain")
                                        hour_chanceofremdry = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceofremdry")
                                        hour_chanceofwindy = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceofwindy")
                                        hour_chanceofovercast = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceofovercast")
                                        hour_chanceofsunshine = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceofsunshine")
                                        hour_chanceoffrost = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceoffrost")
                                        hour_chanceofhightemp = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceofhightemp")
                                        hour_chanceoffog = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceoffog")
                                        hour_chanceofsnow = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceofsnow")
                                        hour_chanceofthunder = response.json().get("data").get("weather")[day].get("hourly")[hour].get("chanceofthunder")
                                        hour_uvIndex = response.json().get("data").get("weather")[day].get("hourly")[hour].get("uvIndex")
                        # 0,12
                        # climate averages
                        for month in range(0,1):
                                month_index = response.json().get("data").get("ClimateAverages")[0].get("month")[month].get("index")
                                month_name = response.json().get("data").get("ClimateAverages")[0].get("month")[month].get("name")
                                month_avgMinTemp = response.json().get("data").get("ClimateAverages")[0].get("month")[month].get("avgMinTemp")
                                month_avgMinTemp_F = response.json().get("data").get("ClimateAverages")[0].get("month")[month].get("avgMinTemp_F")
                                month_absMaxTemp = response.json().get("data").get("ClimateAverages")[0].get("month")[month].get("absMaxTemp")
                                month_absMaxTemp_F = response.json().get("data").get("ClimateAverages")[0].get("month")[month].get("absMaxTemp_F")
                                month_avgDailyRainfall = response.json().get("data").get("ClimateAverages")[0].get("month")[month].get("avgDailyRainfall")
                        # print(url)
                        # lat = str(lat)
                        # lon = str(lon)
                        types = str(types)
                        querys = str(querys)
                        observation_time = str(observation_time)
                        temp_C = str(temp_C)
                        temp_F = str(temp_F)
                        weatherCode = str(weatherCode)
                        weatherIconUrl = str(weatherIconUrl)
                        weatherDesc = str(weatherDesc)
                        windSpeedMiles = str(windSpeedMiles)
                        windSpeedKmph = str(windSpeedKmph)
                        winddirDegree = str(winddirDegree)
                        winddir16Point = str(winddir16Point)
                        precipMM = str(precipMM)
                        humidity = str(humidity)
                        visibility = str(visibility)
                        pressure = str(pressure)
                        cloudcover = str(cloudcover)
                        FeelsLikeC = str(FeelsLikeC)
                        FeelsLikeF = str(FeelsLikeF)
                        uvIndex = str(uvIndex)
                        day_date = str(day_date)
                        day_sunrise = str(day_sunrise)
                        day_sunset = str(day_sunset)
                        day_moonrise = str(day_moonrise)
                        day_moonset = str(day_moonset)
                        day_moon_phase = str(day_moon_phase)
                        day_moon_illumination = str(day_moon_illumination)
                        day_maxtempC = str(day_maxtempC)
                        day_maxtempF = str(day_maxtempF)
                        day_mintempC = str(day_mintempC)
                        day_mintempF = str(day_mintempF)
                        day_totalSnow_cm = str(day_totalSnow_cm)
                        day_sunHour = str(day_sunHour)
                        day_uvIndex = str(day_uvIndex)
                        hour_times = str(hour_times)
                        hour_tempC = str(hour_tempC)
                        hour_tempF = str(hour_tempF)
                        hour_windspeedMiles = str(hour_windspeedMiles)
                        hour_windspeedkmph = str(hour_windspeedkmph)
                        hour_winddirDegree = str(hour_winddirDegree)
                        hour_weatherCode = str(hour_weatherCode)
                        hour_winddir16Point = str(hour_winddir16Point)
                        hour_weatherIconUrl = str(hour_weatherIconUrl)
                        hour_weatherDesc = str(hour_weatherDesc)
                        hour_precipMM = str(hour_precipMM)
                        hour_humidity = str(hour_humidity)
                        hour_visibility = str(hour_visibility)
                        hour_pressure = str(hour_pressure)
                        hour_cloudcover = str(hour_cloudcover)
                        hour_HeatIndexC = str(hour_HeatIndexC)
                        hour_HeatIndexF = str(hour_HeatIndexF)
                        hour_DewPointC = str(hour_DewPointC)
                        hour_DewPointF = str(hour_DewPointF)
                        hour_WindChillC = str(hour_WindChillC)
                        hour_WindChillF = str(hour_WindChillF)
                        hour_WindGustMiles = str(hour_WindGustMiles)
                        hour_WindGustKmph = str(hour_WindGustKmph)
                        hour_FeelsLikeC = str(hour_FeelsLikeC)
                        hour_FeelsLikeF = str(hour_FeelsLikeF)
                        hour_chanceofrain = str(hour_chanceofrain)
                        hour_chanceofremdry = str(hour_chanceofremdry)
                        hour_chanceofwindy = str(hour_chanceofwindy)
                        hour_chanceofovercast = str(hour_chanceofovercast)
                        hour_chanceofsunshine = str(hour_chanceofsunshine)
                        hour_chanceoffrost = str(hour_chanceoffrost)
                        hour_chanceofhightemp = str(hour_chanceofhightemp)
                        hour_chanceoffog = str(hour_chanceoffog)
                        hour_chanceofsnow = str(hour_chanceofsnow)
                        hour_chanceofthunder = str(hour_chanceofthunder)
                        hour_uvIndex = str(hour_uvIndex)
                        month_index = str(month_index)
                        month_name = str(month_name)
                        month_avgMinTemp = str(month_avgMinTemp)
                        month_avgMinTemp_F = str(month_avgMinTemp_F)
                        month_absMaxTemp = str(month_absMaxTemp)
                        month_absMaxTemp_F = str(month_absMaxTemp_F)
                        month_avgDailyRainfall = str(month_avgDailyRainfall)
                        weatherIconUrl="url"
                        hour_weatherIconUrl="url"
                        str1 = "INSERT INTO worldWeather (lat,lon,types,querys,observation_time,temp_C,temp_F,weatherCode,weatherIconUrl,weatherDesc,windSpeedMiles,windSpeedKmph,winddirDegree,winddir16Point,precipMM,humidity,visibility,pressure,cloudcover,FeelsLikeC,FeelsLikeF,uvIndex,day_date,day_sunrise,day_sunset,day_moonrise,day_moonset,day_moon_phase,day_moon_illumination,day_maxtempC,day_maxtempF,day_mintempC,day_mintempF,day_totalSnow_cm,day_sunHour,day_uvIndex,hour_times,hour_tempC,hour_tempF,hour_windspeedMiles,hour_windspeedkmph,hour_winddirDegree,hour_weatherCode,hour_winddir16Point,hour_weatherIconUrl,hour_weatherDesc,hour_precipMM,hour_humidity,hour_visibility,hour_pressure,hour_cloudcover,hour_HeatIndexC,hour_HeatIndexF,hour_DewPointC,hour_DewPointF,hour_WindChillC,hour_WindChillF,hour_WindGustMiles,hour_WindGustKmph,hour_FeelsLikeC,hour_FeelsLikeF,hour_chanceofrain,hour_chanceofremdry,hour_chanceofwindy,hour_chanceofovercast,hour_chanceofsunshine,hour_chanceoffrost,hour_chanceofhightemp,hour_chanceoffog,hour_chanceofsnow,hour_chanceofthunder,hour_uvIndex,month_index,month_name,month_avgMinTemp,month_avgMinTemp_F,month_absMaxTemp,month_absMaxTemp_F,month_avgDailyRainfall) VALUES ('"+lat+"','"+lon+"','"+types+"','"+querys+"','"+observation_time+"','"+temp_C+"','"+temp_F+"','"+weatherCode+"','"+weatherIconUrl+"','"+weatherDesc+"','"+windSpeedMiles+"','"+windSpeedKmph+"','"+winddirDegree+"','"+winddir16Point+"','"+precipMM+"','"+humidity+"','"+visibility+"','"+pressure+"','"+cloudcover+"','"+FeelsLikeC+"','"+FeelsLikeF+"','"+uvIndex+"','"+day_date+"','"+day_sunrise+"','"+day_sunset+"','"+day_moonrise+"','"+day_moonset+"','"+day_moon_phase+"','"+day_moon_illumination+"','"+day_maxtempC+"','"+day_maxtempF+"','"+day_mintempC+"','"+day_mintempF+"','"+day_totalSnow_cm+"','"+day_sunHour+"','"+day_uvIndex+"','"+hour_times+"','"+hour_tempC+"','"+hour_tempF+"','"+hour_windspeedMiles+"','"+hour_windspeedkmph+"','"+hour_winddirDegree+"','"+hour_weatherCode+"','"+hour_winddir16Point+"','"+hour_weatherIconUrl+"','"+hour_weatherDesc+"','"+hour_precipMM+"','"+hour_humidity+"','"+hour_visibility+"','"+hour_pressure+"','"+hour_cloudcover+"','"+hour_HeatIndexC+"','"+hour_HeatIndexF+"','"+hour_DewPointC+"','"+hour_DewPointF+"','"+hour_WindChillC+"','"+hour_WindChillF+"','"+hour_WindGustMiles+"','"+hour_WindGustKmph+"','"+hour_FeelsLikeC+"','"+hour_FeelsLikeF+"','"+hour_chanceofrain+"','"+hour_chanceofremdry+"','"+hour_chanceofwindy+"','"+hour_chanceofovercast+"','"+hour_chanceofsunshine+"','"+hour_chanceoffrost+"','"+hour_chanceofhightemp+"','"+hour_chanceoffog+"','"+hour_chanceofsnow+"','"+hour_chanceofthunder+"','"+hour_uvIndex+"','"+month_index+"','"+month_name+"','"+month_avgMinTemp+"','"+month_avgMinTemp_F+"','"+month_absMaxTemp+"','"+month_absMaxTemp_F+"','"+month_avgDailyRainfall +"');"
                        cur.execute(str1)
                        conn.commit()
                        print("Inserted into worldweather")

                        time.sleep(300)

        ifile.close()
# main
t4 = threading.Thread(target=getCoor, args=(1,))
t4.start()
t4.join()
conn.close()
print("Done")
