from test_foursquare import *
class Collect_data:
	""" Collect data from the json file"""
	def __init__(self, place, city):
		self.data = main(place, city)
		self.city = city
		self.name = []
		self.cities = []
		self.lst = []

	def get_name(self):
		"""
		(self)->(list)
		Return the list of names by the category
		"""
		for i in self.data['venues']:
			for k, v in i.items():
				if k == "name":
					n = i[k]
			self.name.append(n)
		return self.name

	def get_lst(self):
		"""
		(self)->(list)
		Return the list of coordinates of the places
		"""
		lst = [i[k] for i in self.data['venues'] for k, v in i.items() if
			   k == "location"]
		for i in lst:
			for k, v in i.items():
				lt = [i['lat'], i['lng']]
			self.cities.append(lt)
		return self.cities

	def count_places(self):
		return len(self.name)

	def __str__(self):
		return "Names:{}:\nCoordinates:{}".format(self.name, self.cities)

	def __repr__(self):
		return "Names:{}:\nCoordinates:{}".format(self.name, self.cities)


class Compare:
	def __init__(self, place1, place2):
		self.city1 = place1
		self.city2 = place2

	def compare_two(self):
		if self.city1.count_places() > self.city2.count_places():
			return "{} has  more places of that category".format(
				format(self.city1.city))
		else:
			return "{} has  more places of that category".format(
				format(self.city2.city))


a = Collect_data("gym", "Monaco")
a.get_name()
b = Collect_data("gym", "New York City")
b.get_name()
c = Compare(a, b)
print(c.compare_two())

