# Twitter Social Network Crawling and Analysis

The purpose of this project is to familiarize yourself with social network crawling tools and perform various tasks related to Twitter data collection and network analysis. The project is divided into several sections, each requiring different steps and code implementations.

### Section A: Using Gephi to Collect Tweets and Create a Network
- Use Gephi software to collect tweets from Twitter with a desired hashtag and create a network.
- Explain the steps to perform this task.
- Draw the degree distribution diagram of the network.
![communities](https://github.com/MiladAlipour98/Twitter_Crawl/assets/105122009/fa1aee2d-7618-4c49-a380-e3599253d045)
![degree-distribution](https://github.com/MiladAlipour98/Twitter_Crawl/assets/105122009/0bc7106e-bb90-4b98-a72e-fee307fe73b3)
![Eccentricity Distribution](https://github.com/MiladAlipour98/Twitter_Crawl/assets/105122009/67458075-8bd9-4aa5-b4eb-d1ce1f308fe8)
![Harmonic Closeness Centrality Distribution](https://github.com/MiladAlipour98/Twitter_Crawl/assets/105122009/45dfa35f-1a6c-45b2-9b11-7b43fccb23cd)
![Betweenness Centrality Distribut![communities-size-distribution](https://github.com/MiladAlipour98/Twitter_Crawl/assets/105122009/db857870-a475-47c9-82a1-a0cda79c206e)
ion](https://github.com/MiladAlipour98/Twitter_Crawl/assets/105122009/51520ce6-2eef-4681-b538-10c5e1c57ad9)
![Closeness Centrality Distribution](https://github.com/MiladAlipour98/Twitter_Crawl/assets/105122009/7c0ae647-9a09-4a9b-8adc-1b5ecf76fa8a)
![pageranks](https://github.com/MiladAlipour98/Twitter_Crawl/assets/105122009/70fa254f-a45a-45d0-8c28-8d3b8d1a7cd3)

### Section B: Twitter API and Tweet Information Retrieval
- Explain the steps to use the Twitter API.
- Write code that takes a list of tweet IDs and collects information about each tweet.
- If a tweet contains a photo, save the photo.
- Input: a file called "tweets_id.csv" containing Twitter IDs associated with tweets.
- Output: Multiple text files, each named after the tweet ID, containing the corresponding tweet information in JSON format.
- If applicable, save photos with the name of the tweet ID.
- Create a list of user IDs.

### Section C: User Profile Information Retrieval
- Write code that takes a list of user IDs and collects profile information for each user.
- Input: List of user IDs.
- Output: Multiple text files, each named after the Twitter ID of the user, containing the profile information in JSON format.

### Section D: Network Information Retrieval
- Write a crawler that takes a list of user IDs and collects network information.
- Extract the names of friends and followers for each user.
- Output: Multiple files, one for friends and one for followers, named after the Twitter ID of the users.

### Section E: Real-Time Tweet Filtering based on Keywords and Location
- Explain the requirements of this section compared to the previous sections.
- Collect tweets containing either of the two keywords: "ukraine" or "2022worldcup."
- Collect tweets issued within a specific geographical area in Iran.
- Input: Keywords and geographic coordinates.
- Output: Two files, one containing at least 50 tweets filtered by keywords and the other containing at least 50 tweets filtered by geographic coordinates.

### Section F: Crawler for Specific Keyword
- Write a crawler that collects 20 tweets containing the word "Iran" in the tweet text.
- Output: A file in JSON format containing the information of the 50 requested tweets, named "iran.json."

### Section 3: Mentions Network
- Using the Twitter API, write a program to create a network of connections based on mentions in tweets.
- Collect 1000 tweets using the Twitter API and stream tweets online.
- Extract mentions from the tweets.
- Form an undirected author-mention graph, where nodes represent Twitter accounts and edges represent mentions.
- Check the degree distribution of the network and compare it with your prediction.
- Calculate the network diameter, average clustering coefficient, and network density.

