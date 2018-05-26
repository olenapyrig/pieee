import json
import urllib.request
import foursquare


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
#user = client.users()
#print(user)

# Get the user's data
user = client.venues.search(params={'near':'New York City', 'query':  'gym','limit':'5'})


print(user)
