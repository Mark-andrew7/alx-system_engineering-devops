#!/usr/bin/python3
"""
Queries reddit api and returns number of subs
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns number of subscribers
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    user_agent = {'User-Agent': 'custom'}
    response = requests.get(url, headers=user_agent)
    if response.status_code == 200:
        try:
            data = response.json()['data']
            subs = data['subscribers']
            return subs
        except KeyError:
            return 0
    else:
        return 0
