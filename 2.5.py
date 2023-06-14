import tweepy
import json
import csv
import os

def main():
    #Authentication
    os.environ['http_proxy'] = 'socks5://localhost:1080'
    os.environ['https_proxy'] = 'socks5://localhost:1080'
    consumer_key = "Mckank2901pXvBRP3yYer3gUW"
    consumer_secret = "pfiUTxpEO6lGyfUZovx5nTvsAqWAINg2uTTbEAXmT2T8DLaikf"
    access_token = "1264164826185699328-S2Tz9KfXckQivkeSSTi3YwH24GD23l"
    access_token_secret = "JSU6jQ6Art1xPw29v5zGlIxcpcbk2lz98QyLhgwfwoExl"

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