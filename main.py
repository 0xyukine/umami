import os
import sys
import time
import requests
import threading

from dotenv import load_dotenv

from umami.get.post import Post

load_dotenv()
USER = os.getenv('API_USER')
KEY = os.getenv('API_KEY')
FAVOURITES = os.getenv('FAV_URL')

BASE_URL = 'https://e621.net'

def get_listing(s, calls = 1):
	print("Getting listing")
	r = s.get(FAVOURITES + "&limit=30")

	posts = []
	for post in r.json()["posts"]:
		posts.append(Post(post))

	print(posts[0].id, posts[0].tags.general)

def login():
	s = requests.Session()
	s.auth = (USER, KEY)
	s.headers.update({'User-Agent': 'API wrapper (github.com/0xyukine)'})
	get_listing(s)

print("Program currently assumes user has a .env file for username, API key, and favourites URL")
print("Will break currently without the presence of a .env file")
login()
