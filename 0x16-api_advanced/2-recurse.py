#!/usr/bin/python3
"""
Queries Reddit API recursively and returns a list of hot titles
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries Reddit API and returns hot titles
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    user_agent = {'User-Agent': 'custom'}
    params = {'limit': 100}
    response = requests.get(url, headers=user_agent, params=params)

    if response.status_code == 200:
        try:
            data = response.json()['data']['children']
            if not data:
                return hot_list
            else:
                for post in data:
                    hot_list.append(post['data']['title'])
                last_post = data[-1]['data']['name']
                params['after'] = last_post
                return recurse(subreddit, hot_list)
        except KeyError:
            return None
    else:
        return None
