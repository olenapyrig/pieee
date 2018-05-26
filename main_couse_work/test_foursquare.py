import foursquare


def main(place, city):
	"""
	(str,str)->(json)
	Senf request to Forsquare API and return json file with
	the all places found by category in the city
	"""
	client = foursquare.Foursquare(
		client_id='YYNPFYBPCW4D2WDD0CJA0IPG5BWQVZYVVRKUOX1N3HUHK3Y2',
		client_secret='VJPPSVKYFOXTB4LMIPZWJTSDJG0OO3YRAKIHBC1XMOBUVJWG',
		redirect_uri='http://localhost')

	# Build the authorization url for your app
	# auth_uri = client.oauth.auth_url()
	# print('Please open in browser:', auth_uri)
	# resp_code = input('Please enter response code:')

	auth_uri = "https://foursquare.com/oauth2/authenticate?client_id=YYNPFYBPCW4D2WDD0CJA0IPG5BWQVZYVVRKUOX1N3HUHK3Y2&response_type=code&redirect_uri=http%3A%2F%2Flocalhost"
	resp_code = "OOYN4OF2LIFTB3U3RHR4NQMKIAONTDU2DAF3U1OS3YQIV4AV"
	access_token = client.oauth.get_token(resp_code)
	client.set_access_token(access_token)
	user = client.venues.search(
		params={'near': city, 'query': place})
	return user
main("edxf","sdf")