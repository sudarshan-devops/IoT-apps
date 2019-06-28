from Adafruit_IO import Client,Feed,RequestError
from time import sleep
import Adafruit_DHT

ADAFRUIT_IO_KEY="7dd22981c02a44aa84cfc54ce1cc5203"
ADAFRUIT_IO_USERNAME = "gamesbond"
aio=Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)

t=aio.feeds("temp")
h=aio.feeds("humidity")

while True:
    humidity,temperature = Adafruit_DHT.read_retry(11,14)
    print("temperature=%f humidity=%f"%(temperature,humidity))
    aio.send(h.key,humidity)
    aio.send(t.key,temperature)
    sleep(1)

