import pandas as pd

import folium
from geopy.geocoders import Nominatim

def get_coordinates(location):
    """
    Get latitude and longitude for a given location.
    """
    geolocator = Nominatim(user_agent="node_locator")
    loc = geolocator.geocode(location)
    return (loc.latitude, loc.longitude)

def create_map(data):
    """
    Create a world map with nodes annotated.
    """
    world_map = folium.Map(location=[20,0], zoom_start=2)

    for _, row in data.iterrows():
        name, location, description, year = row['Node Name'], row['Location'], row['Description'], row['Year of Establishment']
        lat, lon = get_coordinates(location)
        popup_content = f"<b>{name}</b><br>Location: {location}<br>Description: {description}<br>Year: {year}"
        folium.Marker([lat, lon], popup=popup_content).add_to(world_map)

    return world_map

data = pd.read_excel("C:/Users/pc/PycharmProjects/pythonProject3/pythonProject/OMiLAB/OMiLAB_Nodes_Sorted.xlsx")
create_map(data).save("C:/Users/pc/PycharmProjects/pythonProject3/pythonProject/OMiLAB/map.html")

