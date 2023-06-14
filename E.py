import tweepy
import json
import csv
import os

def main():
    #Authentication
   
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""

    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret, access_token, access_token_secret
    )

    api = tweepy.API(auth)

    if not os.path.isdir("./outputs"):
            os.mkdir("./outputs")
    if not os.path.isdir("./outputs/2.5"):
        os.mkdir("./outputs/2.5")

    with open("./outputs/2.5/iran.json", "w") as keywords_file:
        keywords = ['"Iran"']
        tweets = api.search_tweets(" OR ".join(keywords), count=50, result_type="recent")
        text = [tweet._json for tweet in tweets]
        keywords_file.write(json.dumps(text))

if __name__ == "__main__":
    main()
