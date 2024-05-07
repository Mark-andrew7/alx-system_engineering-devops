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
    user_agent = {'User-agent': 'custom'}
    response = requests.get(url, header=user_agent)
    res = response.json()

    try:
        data = res.requests.get('data')
        subs = data.requests.get('subsribers')
        return subs

    except Exception:
        return 0
