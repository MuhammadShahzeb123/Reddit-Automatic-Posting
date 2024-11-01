from functions import *
import os

client_id = os.getenv("REDDIT_ID")
client_secret = os.getenv("REDDIT_SECRET")
username = os.getenv("REDDIT_USERNAME")
password = os.getenv("REDDIT_PASSWORD")

subreddit_name = "test"
title = "What is this?"
text = "Yo!! How's everybody doing?"


post_to_reddit(subreddit_name, title, text, client_id, client_secret, username, password)