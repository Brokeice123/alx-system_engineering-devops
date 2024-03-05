#!/usr/bin/python3
"""
Function to query the Reddit API and return the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Gets the number of subscribers for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Send a request to the Reddit API
    headers = {'User-Agent': 'Google Chrome Version 120.0.6099.217'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        nb_subscribers = data['data']['subscribers']
        return (nb_subscribers)
    else:
        return (0)
