from twython import Twython, TwythonError
import config

pressed = ''
twitter = Twython(config.APP_KEY, config.APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(config.APP_KEY, access_token=ACCESS_TOKEN)

while pressed == '':

    try:
        results = twitter.search(q='プロ野球')
        print('tweets num:', len(results))
        print(results)
    except TwythonError as e:
        print(e)

    pressed = input("type in enter")

print('finish')
