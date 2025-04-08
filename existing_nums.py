import requests
import json

save_dict = {"bldgs": []}

for i in range(1,9999):
    bldg_num_string = str(i).zfill(4)
    print(bldg_num_string)
    try:
        packet = json.loads(requests.get("https://campusmap.ufl.edu/library/api/bldg", {"bldg":bldg_num_string}).content)
        bothdict = {"ufinfo": packet, "bldgnum": bldg_num_string}
        save_dict["bldgs"].append(bothdict)
    except:
        continue

with open('all_data.json', 'w') as f:
    json.dump(save_dict, f)
