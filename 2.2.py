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

    # b
    with open('tweets_id.csv') as user_ids:
        user_ids = csv.reader(user_ids, delimiter=',')
        user_ids = [row[0] for row in user_ids]
        print(user_ids)

        # create directory
        if not os.path.isdir("./outputs"):
            os.mkdir("./outputs")
        if not os.path.isdir("./outputs/2.2"):
            os.mkdir("./outputs/2.2")

        for user_id in user_ids:
            try:
                user = api.get_user(user_id=user_id)
                with open("./outputs/2.2/{0}.json".format(user.id), "w") as user_file:
                    user_file.write(json.dumps(user._json))
            except Exception:
                pass


if __name__ == "__main__":
    main()
