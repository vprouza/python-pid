import requests
from rich import print
from datetime import datetime
import json


f = open ('conf.json', "r")
config=json.loads(f.read())

api_url = "https://api.golemio.cz/v2"
api_key = config["api_key"]
headers = {"X-Access-Token" : api_key}

print(headers)

api_path = "/pid/departureboards"
#testurl = "/pid/departureboards?ids=U461Z301&minutesBefore=10&minutesAfter=60&timeFrom=2023-06-20T22%3A16%3A00&includeMetroTrains=true&airCondition=true&preferredTimezone=Europe_Prague&mode=departures&order=real&filter=none&skip=canceled&limit=20&total=10&offset=0"


time = datetime.now().isoformat()
print(time)
payload = {
    "ids":"U461Z301", # Uhříněves
    #"ids":"U142Z301", #PHL
    "minutesBefore":"10",
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
    "total":"10",
    "offset":"0"

}


response = requests.get(url=api_url+api_path,headers=headers,params=payload)
print(response.json())

for departure in response.json()["departures"]:
    time = datetime.fromisoformat(departure["departure_timestamp"]["scheduled"]).strftime("%H:%M")
    #print(time)
    print("%s %s %s %s" % (time,departure["route"]["short_name"],str(departure["trip"]["short_name"]),departure["trip"]["headsign"]))
    #print("[red]" + departure["route"]["short_name"] + " " + str(departure["trip"]["short_name"]) + " " + departure["trip"]["headsign"] + " " + departure["departure_timestamp"]["scheduled"])