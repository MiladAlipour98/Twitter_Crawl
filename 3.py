import tweepy
import os
import networkx as nx
import matplotlib.pyplot as plt


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
    if not os.path.isdir("./outputs/3"):
        os.mkdir("./outputs/3")

    with open("./outputs/3/tweets.json", "w") as tweets_file:
        user_dict = {}
        mentions = []
        author = []
        max_id = 0
        while len(user_dict) <= 1000:
            if max_id != 0:
                tweets = api.search_tweets(q=150, count=1000, result_type="recent", max_id=max_id)
            else:
                tweets = api.search_tweets(q=150, count=1000, result_type="recent")

            max_id = tweets.max_id

            a = [tweet.author.screen_name for tweet in tweets]
            for k in a:
                author.append(k)

            l = [tweet.entities['user_mentions'] for tweet in tweets]

            for i in l:
                for j in i:
                 mentions.append(j["screen_name"])

            for tweet in tweets:
                user_dict[tweet.author.screen_name] = user_dict.get(tweet.author.screen_name, [])
                for en in tweet.entities['user_mentions']:
                    user_dict[tweet.author.screen_name].append(en["screen_name"])
                if len(user_dict.get(tweet.author.screen_name)) == 0:
                    user_dict.pop(tweet.author.screen_name)
    for i in range(abs(1000 - len(user_dict))):
        key = list(user_dict.keys())[i]
        user_dict.pop(key)



    print(mentions)
    print(author)
    print(user_dict)

    edge_list = []

    for key in user_dict:

        for i in user_dict[key]:
            edge_list.append((key, i))

    print("edge_list =", edge_list)

    g = nx.Graph(edge_list)

    nx.draw(g, with_labels=True, node_size=20, edge_color='red', node_color='blue', width=0.8, font_size=5)
    plt.show()
    print(nx.is_connected(g))
    ws = []

    S = [g.subgraph(c).copy() for c in nx.connected_components(g)]


    print(ws)
    for w in S:
        ws.append(nx.diameter(w))

    print('diameters=', ws)
    d = max(ws)
    print('diameter=',d)

    c = nx.average_clustering(g)
    density = nx.density(g)


    print('density=',density)
    print('average clustering', c)
    degrees = [g.degree(n) for n in g.nodes()]
    plt.hist(degrees)
    plt.show()



if __name__ == "__main__":
    main()