from geopy.geocoders import ArcGIS
import folium
from collect_data import *
from folium.plugins import MarkerCluster


def map():
	"""Create a HTML map"""
	return folium.Map()


def point(place, city):
	"""The function put points into the map and make the map coloured
	 according to countries' population"""
	map1 = map()
	m = Collect_data(place, city)
	loc = m.get_lst()
	name = m.get_name()
	films = folium.FeatureGroup(name='Films')
	for i, j in zip(loc, name):
		films.add_child(
			folium.Marker(location=i, icon=folium.Icon(), popup=j))
		films.add_child(folium.plugins.HeatMap(loc, name='Coloured Heatmap',
											   max_zoom=25))
		films.add_child(folium.TileLayer())
	map1.add_child(films)
	map1.save("template/map.html")
	return map


# point("gym", "Monaco")
