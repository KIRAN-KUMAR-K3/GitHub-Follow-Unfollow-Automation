
# GitHub-Unfollower

GitHub-Unfollower is a Python script that automatically unfollows all users you're following on GitHub. It uses the GitHub API to streamline the process with built-in rate limit handling.

## Features
- Unfollows all users you're currently following on GitHub.
- Automatically manages GitHub API rate limits to avoid interruptions.
- Simple and easy to use with minimal setup.

## Requirements
- Python 3.x
- `requests` library

## Setup Instructions

### 1. Clone the repository
Clone this repository to your local machine:
```bash
git clone https://github.com/YOUR_USERNAME/GitHub-Unfollower.git
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

### 5. Run the script
Once everything is set up, run the script:
```bash
python run.py
```

The script will fetch the list of users you follow and unfollow them one by one. It handles rate limits by pausing and resuming automatically when needed.

## Example Output
```bash
Successfully unfollowed username1
Successfully unfollowed username2
...
Rate limit exceeded, waiting for 15 minutes.
...
Successfully unfollowed username3
```

## Contribution
Contributions are welcome! Feel free to submit an issue or open a pull request if you'd like to improve the project.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
