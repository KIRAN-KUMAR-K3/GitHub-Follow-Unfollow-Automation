import requests

# Your personal access token (keep it secure)
TOKEN = "ADD YOUR GITHUB-API TOKEN HEAR"

# GitHub API URL for following a user
FOLLOW_URL = "https://api.github.com/user/following"

# Set up the headers with your token
headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

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
    else:
        print(f"Error following {username}: {response.status_code} - {response.text}")

def follow_all_following(target_username):
    """Follow all users that the target user is following."""
    following_users = get_following(target_username)
    
    for username in following_users:
        follow_user(username)

if __name__ == "__main__":
    target_username = "CursedPrograms"  # Target GitHub username
    follow_all_following(target_username)
