import tweepy
from twitter import config

a = tweepy.OAuthHandler("k7TcWQNvLAFw6UHp8b6tjSfys", "HoJ4C5Qgb0kGpt1NkPp4RAuInseNYOHLXOXrpksAU7jwRdW2ZY")
a.set_access_token("105425189-p1Oif8hdJ4RXuN35mbPfH81onaVScOaziCefbRxJ","8gikBBD7lRt7mbGG9JO5Yfy9kMS4OjesrN0UQIZaOEJOI")
a2 = tweepy.API(a)

tt = tweepy.Cursor(a2.search, q="hillary").items(15)
for t in tt:
    print(t.text)

t2 = a2.trends_place(1)

for t in t2[0]["trends"]:
    print(t['name'])