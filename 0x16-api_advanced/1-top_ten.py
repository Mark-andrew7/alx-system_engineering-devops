#!/usr/bin/python3
"""
Queries Reddit API and prints titles of the first 10 hot posts
"""

import requests


def top_ten(subreddit):
    """
    Prints titles of the first 10 hot posts for a given subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    user_agent = {'User-Agent': 'custom'}
    response = requests.get(url, headers=user_agent)

    if response.status_code == 200:
        try:
            data = response.json()['data']['children']
            for post in data[:10]:
                print(post['data']['title'])
        except KeyError:
            print(None)
    else:
        print(None)
