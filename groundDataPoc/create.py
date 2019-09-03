import psycopg2

# conn = psycopg2.connect(database = "testdb2", user = "postgresql", password = "namespace1", host = "sample-database.czgprnseypbr.us-east-1.rds.amazonaws.com", port = "5432")
# conn = psycopg2.connect(database = "weather", user = "postgres", password = "namespace1", hostaddr="35.198.246.100", port = "5432")
# print ('Opened database successfully')
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "namespace1", hostaddr="35.198.246.100", port = "5432")
print ('Opened database successfully')
cur = conn.cursor()


cur.execute('''CREATE TABLE metgispoc(
    lat char(100),
    lon char(100),
    alt char(100),
    sunrise char(100),
    dayCount char(100),
    weatherIcon char(100),
    snowfall char(100),
    unitLin char(100),
    maxTemp char(100),
    description char(100),
    dateRequest char(100),
    windDir char(100),
    sunshineDuration char(100),
    precipitaton char(100),
    windIcon char(100),
    windSpeed char(100),
    lang char(100),
    rainfall char(100),
    unitWind char(100),
    forecastIssued char(100),
    minTemp char(100),
    unitTemp char(100),
    sunset char(100),
    relativeHumidity char(100),
    forecastShortText char(100)
);''')
print("Metgis Created")
cur.execute('''CREATE TABLE openWeatherpoc(
    lat char(50),
    lon char(50),
    id1 char(50),
    main char(50),
    description char(50),
    icon char(50),
    temp char(50),
    pressure char(50),
    humidity char(50),
    temp_min char(50),
    temp_max char(50),
    visibility char(50),
    speed char(50),
    deg char(50),
    clouds char(50),
    dt char(50),
    typ char(50),
    id2 char(50),
    message char(50),
    country char(50),
    sunrise char(50),
    sunset char(50),
    idn char(50),
    name char(50)
);''')
print("openWeather Created")
cur.execute('''CREATE TABLE worldWeatherpoc(
    lat char(50),
    lon char(50),
    types char(50),
    querys char(50),
    observation_time char(50),
    temp_C char(50),
    temp_F char(50),
    weatherCode char(50),
    weatherIconUrl char(50),
    weatherDesc char(50),
    windSpeedMiles char(50),
    windSpeedKmph char(50),
    winddirDegree char(50),
    winddir16Point char(50),
    precipMM char(50),
    humidity char(50),
    visibility char(50),
    pressure char(50),
    cloudcover char(50),
    FeelsLikeC char(50),
    FeelsLikeF char(50),
    uvIndex char(50),
    day_date char(50),
    day_sunrise char(50),
    day_sunset char(50),
    day_moonrise char(50),
    day_moonset char(50),
    day_moon_phase char(50),
    day_moon_illumination char(50),
    day_maxtempC char(50),
    day_maxtempF char(50),
    day_mintempC char(50),
    day_mintempF char(50),
    day_totalSnow_cm char(50),
    day_sunHour char(50),
    day_uvIndex char(50),
    hour_times char(50),
    hour_tempC char(50),
    hour_tempF char(50),
    hour_windspeedMiles char(50),
    hour_windspeedkmph char(50),
    hour_winddirDegree char(50),
    hour_weatherCode char(50),
    hour_winddir16Point char(50),
    hour_weatherIconUrl char(50),
    hour_weatherDesc char(50),
    hour_precipMM char(50),
    hour_humidity char(50),
    hour_visibility char(50),
    hour_pressure char(50),
    hour_cloudcover char(50),
    hour_HeatIndexC char(50),
    hour_HeatIndexF char(50),
    hour_DewPointC char(50),
    hour_DewPointF char(50),
    hour_WindChillC char(50),
    hour_WindChillF char(50),
    hour_WindGustMiles char(50),
    hour_WindGustKmph char(50),
    hour_FeelsLikeC char(50),
    hour_FeelsLikeF char(50),
    hour_chanceofrain char(50),
    hour_chanceofremdry char(50),
    hour_chanceofwindy char(50),
    hour_chanceofovercast char(50),
    hour_chanceofsunshine char(50),
    hour_chanceoffrost char(50),
    hour_chanceofhightemp char(50),
    hour_chanceoffog char(50),
    hour_chanceofsnow char(50),
    hour_chanceofthunder char(50),
    hour_uvIndex char(50),
    month_index char(50),
    month_name char(50),
    month_avgMinTemp char(50),
    month_avgMinTemp_F char(50),
    month_absMaxTemp char(50),
    month_absMaxTemp_F char(50),
    month_avgDailyRainfall char(50)
);''')
print("worldWeather Created")

conn.commit()
conn.close()
