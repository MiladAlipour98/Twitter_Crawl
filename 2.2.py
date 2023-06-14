import tweepy
import json
import csv
import os


def main():
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
