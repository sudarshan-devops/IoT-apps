#!/usr/bin/python
import mysql.connector
import sys
import Adafruit_DHT
import datetime
from time import sleep
db=mysql.connector.connect(user="user",password="passw0rd",host="localhost",database="db1")
cursor = db.cursor()
table=raw_input("enter the name of the table you wish to create")

def dht11():
    count=0
    ch=int(input("enter the logging duration in Seconds"))
    while(count<=ch):
        x = datetime.datetime.now().time()
        humidity, temperature = Adafruit_DHT.read_retry(11, 14)
        print("temperature=%f humidity=%f"%(temperature,humidity)) 
        query="insert into "+table+" values('"+str(x)+"','"+str(temperature)+"','"+str(humidity)+"')"
        results = cursor.execute(query)
        db.commit()
        sleep(1)
        count=count+1

def createtable():
    cursor.execute("drop table if exists "+table)
    sql="create table " +table+ "(DateTime varchar(15),temperature varchar(15),humidity varchar(15))"
    cursor.execute(sql)
    dht11()

createtable()
cursor.close()

