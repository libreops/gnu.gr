import requests
import re


def run_command(msg, *args):
    """Displays a random Chuck Norris joke from http://icndb.com"""
    request = requests.get('http://api.icndb.com/jokes/random')
    joke = request.json()['value']['joke']
    return 'groupchat', re.sub('<[^<]+?>', '', joke)
