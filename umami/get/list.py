import requests

class List():
	def __init__(self):
		pass
	def Search(client, search, page_limit=0, limit=30):
		for page in range(page_limit+1):
			yield client.get("https://e621.net/posts.json?page={}&tags={}&limit={}".format(page,search.replace(" ", "&"),limit)).json()
