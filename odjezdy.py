import requests
from rich import print
from datetime import datetime
import json


f = open ('conf.json', "r")
config=json.loads(f.read())

api_url = "https://api.golemio.cz/v2"
api_key = config["api_key"]
headers = {"X-Access-Token" : api_key}

#print(headers)

api_path = "/pid/departureboards"
#testurl = "/pid/departureboards?ids=U461Z301&minutesBefore=10&minutesAfter=60&timeFrom=2023-06-20T22%3A16%3A00&includeMetroTrains=true&airCondition=true&preferredTimezone=Europe_Prague&mode=departures&order=real&filter=none&skip=canceled&limit=20&total=10&offset=0"


time = datetime.now().isoformat()
print(time)
payload = {
    #"ids":"U461Z301", # Uhříněves
    #"ids":"U142Z301", #PHL
    "ids":["U3316Z1","U3316Z2","U3316Z3","U3316Z4"], # Liběchov
    "minutesBefore":"0",
    "minutesAfter":"1200",
    "timeFrom":time,
    "includeMetroTrains":"false",
    "airCondition":"true",
    "preferredTimezone":"Europe_Prague",
    "mode":"departures",
    "order":"real",
    "filter":"none",
    "skip":"canceled",
    "limit":"20",
    "total":"4",
    "offset":"0"

}


response = requests.get(url=api_url+api_path,headers=headers,params=payload)
print(response.json())

for departure in response.json()["departures"]:
    time = datetime.fromisoformat(departure["departure_timestamp"]["scheduled"]).strftime("%H:%M")
    #print(time)
    print("%s %s %s %s" % (time,departure["route"]["short_name"],str(departure["trip"]["short_name"]),departure["trip"]["headsign"]))
    #print("[red]" + departure["route"]["short_name"] + " " + str(departure["trip"]["short_name"]) + " " + departure["trip"]["headsign"] + " " + departure["departure_timestamp"]["scheduled"])


from PIL import Image, ImageDraw, ImageFont
img = Image.new(mode="RGB",size=(96,48),color=(0,43,89))
font = ImageFont.load("tabule-9.pil")
from unidecode import unidecode

d=ImageDraw.Draw(img)

y=0
for departure in response.json()["departures"]:
    time = datetime.fromisoformat(departure["departure_timestamp"]["scheduled"]).strftime("%H:%M")
    d.text((0,y),time,font=font,fill=(255,255,255))
    #d.text((24,y),str(departure["trip"]["short_name"]),font=font,fill=(255,255,255))
    d.text((26,y),str(departure["route"]["short_name"]),font=font,fill=(255,255,255))
    d.text((48,y),str(unidecode(departure["trip"]["headsign"])),font=font,fill=(255,255,255))
    y+=10
    #d.text((0,10),"Benesov",font=font,fill=(255,255,0))
img.save("img.png")