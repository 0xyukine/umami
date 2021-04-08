import os
import sys
import time
import requests
import threading

from dotenv import load_dotenv

from umami.get.post import Post
from umami.get.list import List

load_dotenv()
USER = os.getenv('API_USER')
KEY = os.getenv('API_KEY')
FAVOURITES = os.getenv('FAV_URL')

BASE_URL = 'https://e621.net'

def get_listing(s, search, calls = 1):
        
        print("Getting listing")
        page_limit = int(input())
        limit = int(input())
        posts = []

        for r in List.Search(s, "fav:tsundereyandere", page_limit, limit):
            for post in r["posts"]:
                posts.append(Post(post))

def neutral(s):
    while True:
        print("Enter 0 to quit or searchterm")
        inp = input()
        if inp == "0":
            sys.exit()
        else:
            get_listing(s, inp)

def login():
        s = requests.Session()
        try:
            load_dotenv()
            USER = os.getenv('API_USER')
            KEY = os.getenv('API_KEY')
        except:
            print("dotenv module not installed or issue with .env file")
            print("Enter details manually? Declining will continue without logging in? (Y/N)")
            inp = input()
            if inp == "Y":
                print("Username:")
                USER = input()
                print("API key:")
                KEY = input()
                s.auth = (USER, KEY)

        s.headers.update({'User-Agent': 'API wrapper (github.com/0xyukine)'})
        neutral(s)

print("Program currently assumes user has a .env file for username, API key, and favourites URL")
print("Will break currently without the presence of a .env file")
login()
