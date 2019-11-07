import twint

c = twint.Config()

tweets = []

c.Limit = 30


c.Store_csv = True
c.Output = "test.csv"
c.Search = "pitangueiras"
c.Format = "Username {username} Mensagem {tweet}"
c.Store_object = True
c.Store_object_tweets_list = tweets

twint.run.Search(c)
n = 0

for tweet in tweets:
    for palavra in tweet.tweet.split(" "):
        print(palavra)
