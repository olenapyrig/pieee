from first_stage import *
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
