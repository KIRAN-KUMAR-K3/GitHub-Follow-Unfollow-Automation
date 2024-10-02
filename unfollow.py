import requests
import time

# Replace with your personal access token
TOKEN = "PAST-YOUR-GITHUB-API-TOKEN"

# GitHub API URL for the authenticated user's following list
FOLLOWING_URL = "https://api.github.com/user/following"
RATE_LIMIT_URL = "https://api.github.com/rate_limit"

# Set up the headers with your token
headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def check_rate_limit():
    """Check remaining rate limit and sleep if necessary."""
    response = requests.get(RATE_LIMIT_URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        remaining = data['resources']['core']['remaining']
        reset_time = data['resources']['core']['reset']
        
        if remaining == 0:
            # Wait for the rate limit to reset
            wait_time = reset_time - time.time()
            print(f"Rate limit exceeded, waiting for {int(wait_time // 60)} minutes.")
            time.sleep(wait_time + 5)  # Sleep for the reset time, with a buffer
    else:
        print(f"Error checking rate limit: {response.status_code}")

def get_following():
    """Fetch the list of users you are currently following."""
    response = requests.get(FOLLOWING_URL, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching following list: {response.status_code}")
        return []

def unfollow_user(username):
    """Unfollow a user by their username."""
    check_rate_limit()  # Check rate limit before making each unfollow request
    unfollow_url = f"{FOLLOWING_URL}/{username}"
    response = requests.delete(unfollow_url, headers=headers)
    
    if response.status_code == 204:
        print(f"Successfully unfollowed {username}")
    else:
        print(f"Error unfollowing {username}: {response.status_code}")

def unfollow_all():
    """Unfollow all users you are following."""
    following = get_following()
    
    if not following:
        print("You are not following anyone.")
        return

    for user in following:
        username = user["login"]
        unfollow_user(username)

if __name__ == "__main__":
    unfollow_all()
