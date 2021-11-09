import json
import urllib
import folium
import pandas as pd
import webbrowser


f = open('vehicles-location.json')
data = json.load(f)

def get_locations():
    locations=[[0]*3]*len(data)

    for i in range (len(data)):
        location = [0]*3
        location[0]=data[i]['location']['lat']
        location[1] = data[i]['location']['lng']
        location[2] = data[i]['location']['bearing']
        locations[i]=location
    return locations

def get_cars_in_location(leftlow,lefthigh,right,righthigh):
    return 0

def show_map():
    map = folium.Map(location=[51.507351, -0.127758],zoom_start=8)
    for car in data:
        folium.Marker(location= [car['location']['lat'], car['location']['lng']], popup=car['id']).add_to(map)
    map.save('index.html')
    webbrowser.open('index.html')

show_map()






