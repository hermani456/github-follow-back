import os
import requests

GITHUB_USERNAME = os.getenv("GH_USERNAME")
GITHUB_TOKEN = os.getenv("GH_TOKEN")

def get_all_items(url):
    items = []
    page = 1
    while True:
        params = {'page': page, 'per_page': 100}
        response = requests.get(url, auth=(GITHUB_USERNAME, GITHUB_TOKEN), params=params)
        if response.status_code != 200:
            print(f"Error fetching data: {response.status_code} {response.json()}")
            break
        data = response.json()
        if not data:
            break
        items.extend(data)
        page += 1
    return items

def get_followers(username):
    url = f"https://api.github.com/users/{username}/followers"
    data = get_all_items(url)
    return {item['login'] for item in data}

def get_following(username):
    url = f"https://api.github.com/users/{username}/following"
    data = get_all_items(url)
    return {item['login'] for item in data}

def follow_user(username):
    url = f"https://api.github.com/user/following/{username}"
    response = requests.put(url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    if response.status_code == 204:
        print(f"Followed {username}")
    else:
        print(f"Failed to follow {username}: {response.status_code} {response.json()}")

def unfollow_user(username):
    url = f"https://api.github.com/user/following/{username}"
    response = requests.delete(url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    if response.status_code == 204:
        print(f"Unfollowed {username}")
    else:
        print(f"Failed to unfollow {username}: {response.status_code} {response.json()}")

def main():
    followers = get_followers(GITHUB_USERNAME)
    following = get_following(GITHUB_USERNAME)

    to_follow = followers - following
    for user in to_follow:
        follow_user(user)

    to_unfollow = following - followers
    for user in to_unfollow:
        unfollow_user(user)

if __name__ == '__main__':
    main()