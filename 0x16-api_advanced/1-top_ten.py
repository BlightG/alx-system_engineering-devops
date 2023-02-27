#!/usr/bin/python3
"""
a module housing a function that interacts with the reddit api
"""
import requests


def top_ten(subreddit):
    """
    a function the returns the top 10 popular posts for a given subreddit
    args:
        subreddit - name of a subreddit
    Return:
        returns popular posts of the subreddit or
        None if an invalid subreddit is passed.
    """
    if subreddit is None:
        return None

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                             AppleWebKit/537.36 (KHTML, like Gecko)\
                             Chrome/102.0.0.0 Safari/537.36'}

    with requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json',
                      headers=headers, params={'limit': '8'}) as res:

        if res.status_code == 200:
            res_json = res.json()
            if 'data' in res_json.keys():
                i = 1
                for lst in res_json['data']['children']:
                    print(str(i) + ' ' + lst['data']['title'])
                    i += 1
            else:
                print("None")
        else:
            print("None")
