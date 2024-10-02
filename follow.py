import requests
import time
import json

# Load configuration from a JSON file
def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

# Get configuration settings
config = load_config()
TOKEN = config["TOKEN"]
TARGET_USERNAME = config["TARGET_USERNAME"]

# GitHub API URL for following a user
FOLLOW_URL = "https://api.github.com/user/following"

# Set up the headers with your token
headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def check_rate_limit():
    """Check the current rate limit status."""
    response = requests.get("https://api.github.com/rate_limit", headers=headers)
    if response.status_code == 200:
        limits = response.json()
        remaining = limits['rate']['remaining']
        reset_time = limits['rate']['reset']
        return remaining, reset_time
    else:
        print(f"Error checking rate limit: {response.status_code} - {response.text}")
        return 0, None

def get_following(username):
    """Get a list of users that a specified user is following."""
    url = f"https://api.github.com/users/{username}/following"
    following = []

    while url:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            following.extend(user['login'] for user in response.json())
            # Check for pagination
            url = response.links.get('next', {}).get('url')
        else:
            print(f"Error fetching following for {username}: {response.status_code} - {response.text}")
            break
    
    return following

def follow_user(username):
    """Follow a user by their username."""
    follow_url = f"{FOLLOW_URL}/{username}"
    response = requests.put(follow_url, headers=headers)

    if response.status_code == 204:
        print(f"Successfully followed {username}")
    elif response.status_code == 404:
        print(f"User {username} not found. Skipping...")
    else:
        print(f"Error following {username}: {response.status_code} - {response.text}")

def follow_all_following(target_username):
    """Follow all users that the target user is following."""
    following_users = get_following(target_username)

    for username in following_users:
        # Check rate limit before each follow
        remaining, reset_time = check_rate_limit()
        if remaining <= 0:
            wait_time = max(0, reset_time - int(time.time()))
            print(f"Rate limit exceeded. Waiting for {wait_time} seconds...")
            time.sleep(wait_time + 5)  # Wait until reset + buffer time

        follow_user(username)

if __name__ == "__main__":
    follow_all_following(TARGET_USERNAME)
