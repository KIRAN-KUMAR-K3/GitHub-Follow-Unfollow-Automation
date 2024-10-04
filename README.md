
# 🚀 GitHub Follow/Unfollow Automation

**GitHub-Follow-Unfollow-Automation** is a Python script that simplifies the process of following and unfollowing users on GitHub. With this tool, you can easily manage your followers list, leveraging the GitHub API for bulk actions while keeping API rate limits in check.

## ✨ Features

- **📤 Unfollow All**: Automatically unfollows everyone you're currently following on GitHub.
- **📥 Bulk Follow**: Follow a pre-defined list of GitHub users with ease.
- **⏱️ Rate Limit Handling**: Automatically pauses and resumes operations based on GitHub's API rate limits.
- **⚡ Quick Setup**: Requires minimal configuration, making it super easy to get started.

---

## 🛠️ Requirements

Ensure you have the following installed:

- **Python 3.x**
- **requests** library

---

## 🚀 Quick Setup

Follow these steps to get up and running:

### 1. Clone the Repository

```bash
git clone https://github.com/KIRAN-KUMAR-K3/GitHub-Follow-Unfollow-Automation.git
```

### 2. Install Dependencies

Install the necessary Python libraries:

```bash
pip install requests
```

### 3. Generate Your GitHub Personal Access Token (PAT)

- Go to **GitHub Settings** > **Developer Settings** > **Personal Access Tokens**.
- Generate a new token with **Fine-grained access** and give it the necessary permissions (like repository access and follower management).

### 4. Configure the Script

In `run.py`, update the placeholder with your generated GitHub token:

```python
TOKEN = "your_personal_access_token_here"
```

Also, specify the list of GitHub users you wish to follow:

```python
usernames_to_follow = ["username1", "username2", "username3"]
```

### 5. Run the Script

You’re now ready to run the script. Use the following commands:

- **Follow users**:

  ```bash
  python follow.py
  ```

- **Unfollow all users**:

  ```bash
  python unfollow.py
  ```

The script handles GitHub API rate limits and resumes operations after waiting for the required cooldown time.

### 🖥️ Example Output

```
Unfollowing username1... Success
Unfollowing username2... Success
Following username3... Success
...
Rate limit exceeded. Pausing for 15 minutes...
...
Resuming... Successfully followed username4.
```

---

## 🤝 Contribute

Want to help improve this project? Contributions are always welcome! Feel free to:

- Open an **Issue** for any bugs or suggestions.
- Submit a **Pull Request** to enhance functionality or fix issues.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE). For more details, refer to the license file.

---
