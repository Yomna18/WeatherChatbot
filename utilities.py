import mysql.connector as mysql
import datetime
import requests



mydb = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="projectchatbot"
)


def doesUserExist(user):
    cur = mydb.cursor(dictionary=True)
    qry = "SELECT * FROM `user` WHERE `UserName`= '{}'".format(user)
    cur.execute(qry)
    result = cur.fetchone()
    return False if result is None else True


def registerUser(user, Password):
    cur = mydb.cursor()
    sql = "INSERT INTO user (UserName, Password) VALUES (%s, %s)"
    val = (user, Password)
    cur.execute(sql, val)
    mydb.commit()
    print(cur.rowcount, "record inserted.")
    return True


def authenticateUser(user, Password):
    cur = mydb.cursor(dictionary=True)
    qry = "SELECT * FROM `user` WHERE `UserName`= '{}' AND `Password`= {}".format(user, Password)
    cur.execute(qry)
    user = cur.fetchone()
    print(user)
    return False if user is None else True



def ShowWeather(city):

    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=6efcac7369304c8ede18e8db962e1187"
    json_data = requests.get(api).json()
    
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp']-273.15)
    min_temp = int(json_data['main']['temp_min']-273.15)
    max_temp = int(json_data['main']['temp_max']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data["wind"]["speed"]

    return condition, temp, min_temp, max_temp, pressure, humidity, wind
