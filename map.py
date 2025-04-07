import simplekml
import json

kml = simplekml.Kml()

with open("bldg_data.json") as f:
    json = json.load(f)

for building in json["bldgs"]:
    kml.newpoint(name=building["ufinfo"]["NAME"], description=building["bldgnum"], coords=[(building["locinfo"]["lng"], building["locinfo"]["lat"])])

kml.save("ufbuildings.kml")
