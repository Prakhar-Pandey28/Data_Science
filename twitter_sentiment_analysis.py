import tweepy
from textblob import TextBlob

# Replace with your actual keys and tokens
consumer_key = '82evv2hm60ovrRwbwU6oPPwpT'
consumer_secret = 'Z8D8l2kfELSLmdOUIhkhIdPRpPtwZtgz4y5awGdTN8pdixUPOL'
access_token = '1403981177141088262-IiXvXockdGEOG7pQb4ObmmAeG1GUtk'
access_token_secret = 'M4D455tqz2qVjMITZVPzARjdvGMuSLHCcHfUSPnIJUdwM'

# Authenticate using Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API client
api = tweepy.API(auth)

# Twitter API v2 client (for search_recent_tweets)
bearer_token = 'AAAAAAAAAAAAAAAAAAAAACyPxAEAAAAAHBVDY1%2BTACCzpqr6kiwx4U55L5o%3DY8pHXh5naft45uKdYXgyGPiuhihScwgRUHYHwPdI9eEsof9kxz'  # Obtain this from the Twitter Developer Portal
client = tweepy.Client(bearer_token=bearer_token)

# Search for tweets containing the word 'Trump' using the Twitter API v2
query = "Modi -is:retweet"  # Exclude retweets
tweets = client.search_recent_tweets(query=query, max_results=10)  # Adjust max_results as needed

# Process and analyze tweets
for tweet in tweets.data:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
