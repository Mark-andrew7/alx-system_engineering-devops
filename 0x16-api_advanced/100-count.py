#!/usr/bin/python3
"""
Queries Reddit API recursively and prints a sorted count
"""

import requests


def count_words(subreddit, word_list, word_count={}):
    """
    Recursively queries Reddit API and prints a sorted count
    """
    if subreddit is None or not isinstance(subreddit, str) or not word_list:
        return

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    user_agent = {'User-Agent': 'custom'}
    params = {'limit': 100}
    response = requests.get(url, headers=user_agent, params=params)

    if response.status_code == 200:
        try:
            data = response.json()['data']['children']
            if not data:
                sorted_results = sorted(word_count.items(), key=lambda x:
                                        (-x[1], x[0]))
                for word, count in sorted_results:
                    print(f"{word}: {count}")
                return
            else:
                for post in data:
                    title = post['data']['title']
                    for word in word_list:
                        if word.lower() in title.lower().split():
                            word_count[word.lower()] =
                            word_count.get(word.lower(), 0) + 1
                last_post = data[-1]['data']['name']
                params['after'] = last_post
                return count_words(subreddit, word_list, word_count)
        except KeyError:
            return
    else:
        return
