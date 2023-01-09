import tweepy
from dotenv import load_dotenv

api_key = config.API_key
api_secret = config.API_secret
user_key = config.Access_token
user_secret = config.Access_secret

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
client = tweepy.Client(bearer_token=config.Bearer_token)

# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)
  
# calling the api 
api = tweepy.API(auth)
  
# the profile name to be updated
name = "api test"

user_profile = api.update_profile(name)