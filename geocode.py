import requests
import json
from dotenv import load_dotenv
from os import getenv

load_dotenv()
api_key = getenv("API_KEY")

save_dict = {"bldgs": []}
with open("all_data.json") as f:
    bldg_json = json.load(f)
    
for i, bldg in enumerate(bldg_json["bldgs"]):
    try:
        print(bldg["bldgnum"], bldg["ufinfo"]["NAME"])
        coords = json.loads(requests.get("https://maps.googleapis.com/maps/api/geocode/json", {"address": bldg["ufinfo"]["ADDRESS1"] + ' ' + bldg["ufinfo"]["ADDRESS2"] + ' ' + bldg["ufinfo"]["CITY"], "key": api_key}).content)["results"][0]["geometry"]["location"]
        topleveldict = {"ufinfo": bldg["ufinfo"], "locinfo": coords, "bldgnum": bldg["bldgnum"]}
        save_dict["bldgs"].append(topleveldict)
    except:
        continue
    if not i % 100:
        with open('all_loc_data.json', 'w') as f:
            json.dump(save_dict, f)
with open('all_loc_data.json', 'w') as f:
            json.dump(save_dict, f)

