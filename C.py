import tweepy
import json
import csv
import os

def main():
   
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""

    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret, access_token, access_token_secret
    )

    api = tweepy.API(auth)
    with open('tweets_id.csv') as user_ids:
        user_ids = csv.reader(user_ids, delimiter=',')
        user_ids = [row[0] for row in user_ids]
        print(user_ids)

    if not os.path.isdir("./outputs"):
        os.mkdir("./outputs")
    if not os.path.isdir("./outputs/2.3"):
        os.mkdir('./outputs/2.3')
    if not os.path.isdir("./outputs/2.3/followers"):
        os.mkdir("./outputs/2.3/followers")
    if not os.path.isdir("./outputs/2.3/friends"):
        os.mkdir("./outputs/2.3/friends")

    for user_id in user_ids:
        try:
            with open("./outputs/2.3/followers/{0}.json".format(user_id), "w") as user_followers:
                followers = api.get_follower_ids(user_id=user_id, count=20)
                user_followers.write(json.dumps(followers))
            with open("./outputs/2.3/friends/{0}.json".format(user_id), "w") as user_friends:
                friends = api.get_friend_ids(user_id=user_id, count=20)
                user_friends.write(json.dumps(friends))
        except Exception:
            pass

if __name__ == "__main__":
    main()
