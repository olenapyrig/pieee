import foursquare


def main():
	d = {}
	client = foursquare.Foursquare(
		client_id='YYNPFYBPCW4D2WDD0CJA0IPG5BWQVZYVVRKUOX1N3HUHK3Y2',
		client_secret='VJPPSVKYFOXTB4LMIPZWJTSDJG0OO3YRAKIHBC1XMOBUVJWG',
		redirect_uri='http://localhost')

	# Build the authorization url for your app
	auth_uri = client.oauth.auth_url()
	print('Please open in browser:', auth_uri)
	resp_code = input('Please enter response code:')

	# Interrogate foursquare's servers to get the user's access_token
	access_token = client.oauth.get_token(resp_code)
	# Apply the returned access token to the client
	client.set_access_token(access_token)
	# user = client.users()
	user = client.venues.search(
		params={'near': 'New York City', 'query': 'gym', 'limit': '5'})
	return user


def get_name(data):
	lst = []
	for i in data['venues']:
		for k, v in i.items():
			if k == "name":
				n = i[k]
		lst.append(n)
	return lst


def get_dct(data):
	lst = []
	for i in data['venues']:
		for k, v in i.items():
			if k == "location":
				lst.append(i[k])
	return lst


def get_loc(data):
	lst = []
	for i in data:
		for k, v in i.items():
			lt = [i['lat'], i['lng']]
		lst.append(lt)
	return lst


def create_dct(name, loc):
	d = {}
	for i in name:
		for k in loc:
			d[i] = k
	return d
# print(create_dct(get_name(main()), get_loc(get_dct(main()))))
