
# GitHub Follow/Unfollow Automation

**GitHub-Follow-Unfollow-Automation** is a Python script designed to automate the processes of following and unfollowing users on GitHub. By leveraging the GitHub API, this tool efficiently manages API rate limits while performing bulk actions seamlessly.

## Features

- **Unfollow**: Unfollows all users you are currently following on GitHub.
- **Follow**: Follows a list of specified users on GitHub.
- **Rate Limit Management**: Automatically handles GitHub API rate limits to prevent interruptions.
- **Simple Setup**: User-friendly with minimal configuration required.

## Requirements

- **Python 3.x**
- **requests library**

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/KIRAN-KUMAR-K3/GitHub-Follow-Unfollow-Automation.git
```

### 2. Install Dependencies

Ensure that the `requests` library is installed. You can install it by running:

```bash
pip install requests
```

### 3. Generate a GitHub Personal Access Token

To use the GitHub API, create a personal access token (PAT) by following these steps:

- Navigate to **GitHub Settings**.
- Click on **Generate new token**.
- Choose **Fine-grained access tokens** and set the required permissions:
  - **Repository access**: All repositories or specific ones as needed.
  - **Account permissions**: Select "Followers" to manage who you follow.
- Click **Generate token** and copy the token (it will only be displayed once).

### 4. Configure the Script

In the `run.py` file, replace the placeholder `TOKEN` with your personal access token:

```python
# Replace with your personal access token
TOKEN = "your_personal_access_token_here"
```

Additionally, specify the list of users you want to follow:

```python
# List of usernames to follow
usernames_to_follow = ["username1", "username2", "username3"]
```

### 5. Run the Script

Once everything is set up, you can run the script:

- To **Follow**:

  ```bash
  python follow.py
  ```

- To **Unfollow**:

  ```bash
  python unfollow.py
  ```

The script will first unfollow all users you are following, then proceed to follow the specified users. It automatically manages rate limits by pausing and resuming as needed.

### Example Output

```
Successfully unfollowed username1
Successfully unfollowed username2
Successfully followed username3
...
Rate limit exceeded, waiting for 15 minutes.
...
Successfully followed username4
```

## Contribution

Contributions are welcome! Feel free to submit an issue or open a pull request if you would like to improve this project.

## License

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for more details.
