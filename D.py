import tweepy
import json
import csv
import os
from math import sin, acos, cos, radians

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
    if not os.path.isdir("./outputs/2.4"):
        os.mkdir("./outputs/2.4")

    with open("./outputs/2.4/filtered_by_keywords.txt", "w") as keywords_file:
        keywords = ["#worldcup2022", "#ukraine"]
        tweets = api.search_tweets(" OR ".join(keywords), count=100, result_type="recent")
        for tweet in tweets:
            keywords_file.write(json.dumps(tweet._json))

    with open("./outputs/2.4/filtered_by_geo.txt", "w") as geo_file:
        points = [(36.385913, 47.526684), (30.524413, 58.512660)]
        center = ((points[0][0] + points[1][0])/2, (points[0][1] + points[1][1])/2)
        radius = 0.5 * 6371.01 * acos(sin(radians(points[0][0]))*sin(radians(points[1][0])) + cos(radians(points[0][0]))*cos(radians(points[1][0])*cos(radians(points[0][1])) - radians(points[1][1])))
        tweets = api.search_tweets('', geocode="{0},{1},{2}km".format(center[0], center[1], radius), count=100, result_type="recent")
        for tweet in tweets:
            geo_file.write(json.dumps(tweet._json))

if __name__ == "__main__":
    main()
