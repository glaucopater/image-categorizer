import requests

api_key = 'acc_3d59c7c967cc508'
api_secret = '24e68357cec839604ea30a2ee5537271'
image_url = 'http://docs.imagga.com/static/images/docs/sample/japan-605234_1280.jpg'

response = requests.get('https://api.imagga.com/v2/tags?image_url=%s' % image_url,
                auth=(api_key, api_secret))

print (response.json())