from datetime import datetime, timedelta
import random

min_delta = timedelta(hours=1)
start = datetime.now()
messages = [
    '{} has left the room? Lucky us!',
    'Fortunately {} went voluntarily',
    'Finally {} has left the room',
]


def muc_got_offline(nick):
    global start
    if (datetime.now() - start) > min_delta:
        start = datetime.now()
        return random.choice(messages).format(nick)
