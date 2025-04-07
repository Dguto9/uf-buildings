import requests
import json
from dotenv import load_dotenv
from os import getenv

load_dotenv()
api_key = getenv("API_KEY")

save_dict = {"bldgs": []}

for i in range(1,1502):
    bldg_num_string = str(i).zfill(4)
    print(bldg_num_string)
    try:
        packet = json.loads(requests.get("https://campusmap.ufl.edu/library/api/bldg", {"bldg":bldg_num_string}).content)
        coords = json.loads(requests.get("https://maps.googleapis.com/maps/api/geocode/json", {"address": packet["ADDRESS1"] + ' ' + packet["ADDRESS2"] + ' ' + packet["CITY"], "key": api_key}).content)["results"][0]["geometry"]["location"]
        bothdict = {"ufinfo": packet, "locinfo": coords, "bldgnum": bldg_num_string}
        save_dict["bldgs"].append(bothdict)
        # bldgs.append((packet["ADDRESS1"], packet["NAME"]))
    except:
        continue

with open('bldg_data.json', 'w') as f:
    json.dump(save_dict, f)
