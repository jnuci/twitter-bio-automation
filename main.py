import tweepy
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("API_key")
api_secret = os.getenv("API_secret")
user_key = os.getenv("Access_token")
user_secret = os.getenv("Access_secret")

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(api_key, api_secret)

# set access to user's access key and access secret 
auth.set_access_token(user_key, user_secret)
  
# calling the api 
api = tweepy.API(auth)
  
# the profile name to be updated
text = "api test"

api.update_profile(description = text)