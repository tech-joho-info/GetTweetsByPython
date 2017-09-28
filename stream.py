from twython import TwythonStreamer, TwythonError

import config

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'])

    def on_error(self, status_code, data):
        print(status_code)

try:
    stream = MyStreamer(config.APP_KEY, config.APP_SECRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    stream.statuses.filter(track='AKB48')

except TwythonError as e:
    print(e)