import requests

class List():
	def __init__(self):
		pass
	def Search(client, search, limit=30):
		return client.get("https://e621.net/posts.json?&tags={}&limit={}".format(search.replace(" ", "&"),limit)).json()
