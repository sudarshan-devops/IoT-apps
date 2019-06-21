import datetime
import xlwt
import sys
import Adafruit_DHT
from time import sleep
count=1
while(count<=5):
    x = datetime.datetime.now()
    humidity, temperature = Adafruit_DHT.read_retry(11, 21)
    DATA = (("Temperature", temperature,),
            ("Humidity", humidity,),)
    wb = xlwt.Workbook()
    ws = wb.add_sheet("My Sheet")
    for i, row in enumerate(DATA):
        for j, col in enumerate(row):
            ws.write(i, j, col)
    ws.col(0).width = 256 * max([len(row[0]) for row in DATA])
    wb.save("myworkbook.xls")
    print(x)
    sleep(1)
    count=count+1
