import requests

class List():
	def __init__(self):
		pass
	def Search(client, search):
		search = "https://e621.net/posts.json?&tags=" + search
		return client.get(search + "&limit=30").json()