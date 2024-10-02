
# GitHub-Follow-Unfollow-Automation

GitHub-Follow-Unfollow-Automation is a Python script that allows users to automatically follow and unfollow users on GitHub. It utilizes the GitHub API to streamline both processes while effectively managing API rate limits.

## Features
- **Unfollow**: Unfollows all users you're currently following on GitHub.
- **Follow**: Follows a list of specified users on GitHub.
- **Rate Limit Management**: Automatically handles GitHub API rate limits to avoid interruptions.
- **Simple Setup**: Easy to use with minimal configuration.

## Requirements
- Python 3.x
- `requests` library

## Setup Instructions

### 1. Clone the repository
Clone this repository to your local machine:
```bash
git clone https://github.com/KIRAN-KUMAR-K3/GitHub-Follow-Unfollow-Automation.git
```

### 2. Install dependencies
Ensure that the `requests` library is installed. You can install it by running:
```bash
pip install requests
```

### 3. Generate a GitHub Personal Access Token
To use the GitHub API, you will need to create a personal access token (PAT).

#### Steps:
- Go to [GitHub settings](https://github.com/settings/tokens).
- Click on **Generate new token**.
- Choose **Fine-grained access tokens** and set these permissions:
  - **Repository access**: All repositories or the specific ones you need.
  - **Account permissions**: Select "Followers" to manage who you follow.
- Click **Generate token** and copy the token (it will only be shown once).

### 4. Configure the script
In the `run.py` file, replace the placeholder `TOKEN` with your personal access token:
```python
# Replace with your personal access token
TOKEN = "your_personal_access_token_here"
```

Additionally, you can specify the list of users you want to follow in the script:
```python
# List of usernames to follow
usernames_to_follow = ["username1", "username2", "username3"]
```

### 5. Run the script
Once everything is set up, you can run the script:

*To Follow*
```bash
python follow.py
```
*To Unfollow*
```bash
python unfollow.py
```

The script will first unfollow all users you're following and then proceed to follow the specified users. It handles rate limits by pausing and resuming automatically when needed.

## Example Output
```bash
Successfully unfollowed username1
Successfully unfollowed username2
Successfully followed username3
...
Rate limit exceeded, waiting for 15 minutes.
...
Successfully followed username4
```

## Contribution
Contributions are welcome! Feel free to submit an issue or open a pull request if you'd like to improve the project.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
