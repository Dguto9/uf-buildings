import simplekml
import json

kml = simplekml.Kml()

with open("all_loc_data.json") as f:
    json = json.load(f)

for building in json["bldgs"]:
    kml.newpoint(description=building["bldgnum"] + '\n' + building["ufinfo"]["NAME"], coords=[(building["locinfo"]["lng"], building["locinfo"]["lat"])])

kml.save("ufbuildings_all.kml")
