from pathlib import Path
import json
import plotly.express as px
# Read data as a string and convert to a Python object.
path = Path('data/schools-list.geojson')
contents = path.read_text()
data = json.loads(contents)

#path = Path('data/readable_data_school.geojson')
#readable_data = json.dumps(data, indent=4)
#path.write_text(readable_data)

s_names, strengths, lons, lats, statuses = [], [], [], [], []
all_scl_dicts = data["features"]
for scl_dict in all_scl_dicts:
    establishment = scl_dict["properties"]["Establishment"]
    pupil = scl_dict["properties"]["Number of pupils on roll"]
    lon = scl_dict["geometry"]["coordinates"][0]
    lat = scl_dict["geometry"]["coordinates"][1]
    status = scl_dict["properties"]["Status"]
    s_names.append(establishment)
    strengths.append(int(pupil))
    lons.append(lon)
    lats.append(lat)
    statuses.append(status)


fig = px.scatter_geo(lat = lats, lon = lons,  title= "Schools locations",
                     color = strengths,
                     color_continuous_scale= "Viridis",
                     labels={ "color" : "Strength"},
                     hover_name= s_names, )
fig.show()
