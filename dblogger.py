#!/usr/bin/python
import MySQLdb
import sys
import Adafruit_DHT
import datatime
from time import sleep
db=MySQLdb.connect("localhost","root","12345","testdb")
cursor = db.cursor()
createtale()
count=0
def dht11():
    ch=int(input("enter the logging duration in Seconds"))
    while(count<=ch):
        x = datetime.datetime.now()
        humidity, temperature = Adafruit_DHT.read_retry(11, 21)
        print(temperature, humidity)
        query="insert into "+table+" values("+x+","+temperature+","+humidity+")"
        cursor.execute(query)
        sleep(1)
        count=count+1

def createtable():
    table=input("enter the name of table you wish to create")
    cursor.execute("drop table if exists "+table)
    sql="create table " +table+ "(DateTime varchar(15),temperature varchar(5),humidity varchar(5))"
    cursor.execute(sql)

db.close()

