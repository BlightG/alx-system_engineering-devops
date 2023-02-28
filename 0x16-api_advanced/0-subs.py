#!/usr/bin/python3
'''a module housing a function that interacts with the reddit api'''


import requests


def number_of_subscribers(subreddit):
    """
       a function the returns the number of subscribers of a subreddit
       args:
           subreddit - name of a subreddit
       Return:
           returns number of subscribers to the subreddit or
           0 if an invalid subreddit is passed.
    """
    if subreddit is None:
        return 0

    headers = {'User-Agent':
                               'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/102.0.0.0 Safari/537.36'}
    with requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                      headers=headers, allow_redirects=False) as res:
        if res.status_code == 200:
            res_json = res.json()
            if 'subscribers' in res_json['data'].keys():
                return res.json()['data']['subscribers']
        return (0)
