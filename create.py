import psycopg2

conn = psycopg2.connect(database = "testdb2", user = "postgresql", password = "namespace1", host = "sample-database.czgprnseypbr.us-east-1.rds.amazonaws.com", port = "5432")
print ('Opened database successfully')
cur = conn.cursor()


cur.execute('''CREATE TABLE metgis(
    lat char(10),
    lon char(10),
    alt char(10),
    sunrise char(10),
    dayCount char(10),
    weatherIcon char(10),
    snowfall char(10),
    unitLin char(10),
    maxTemp char(10),
    description char(10),
    dateRequest char(10),
    windDir char(10),
    sunshineDuration char(10),
    precipitaton char(10),
    windIcon char(10),
    windSpeed char(10),
    lang char(10),
    rainfall char(10),
    unitWind char(10),
    forecastIssued char(10),
    minTemp char(10),
    unitTemp char(10),
    sunset char(10),
    relativeHumidity char(10),
    forecastShortText char(10)
);''')
print("Metgis Created")
cur.execute('''CREATE TABLE openWeather(
    lat char(10),
    lon char(10),
    id1 char(10),
    main char(10),
    description char(10),
    icon char(10),
    temp char(10),
    pressure char(10),
    humidity char(10),
    temp_min char(10),
    temp_max char(10),
    visibility char(10),
    speed char(10),
    deg char(10),
    clouds char(10),
    dt char(10),
    typ char(10),
    id char(10),
    message char(10),
    country char(10),
    sunrise char(10),
    sunset char(10),
    idn char(10),
    name char(10)
);''')
print("openWeather Created")
cur.execute('''CREATE TABLE worldWeather(
    lat char(10),
    lon char(10),
    types char(10),
    querys char(10),
    observation_time char(10),
    temp_C char(10),
    temp_F char(10),
    weatherIconUrl char(10),
    weatherDesc char(10),
    windSpeedMiles char(10),
    windSpeedKmph char(10),
    winddirDegree char(10),
    winddir16Point char(10),
    precipMM char(10),
    humidity char(10),
    visibility char(10),
    pressure char(10),
    cloudcover char(10),
    FeelsLikeC char(10),
    FeelsLikeF char(10),
    uvIndex char(10)
);''')
print("worldWeather Created")

# conn.commit()
# conn.close()
