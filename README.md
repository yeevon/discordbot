# 🛠 Discord GitHub Webhook Bot
A lightweight Python bot that listens for GitHub webhook events (e.g. Pull Requests) and posts updates to a designated Discord channel. Built using discord.py and Flask, and deployed on AWS for live operation.

----
## ✅ Key Features
- Receives GitHub webhook events (e.g. pull request opened, closed, merged).

- Posts a formatted message with the PR title, user, and link to the configured Discord channel.

- Combines asynchronous Discord bot functionality with a Flask webhook server.

- Deployed on AWS (e.g., EC2 or Lightsail) for 24/7 availability.

## 📦 Technologies Used
- Python 3

- discord.py

- Flask

- dotenv for secure configuration

- AWS (EC2, Lightsail, etc.) for deployment

## 🚀 How It Works
1. GitHub sends a webhook POST request to /webhook.

2. Flask processes the JSON payload and extracts PR data.

3. Discord bot formats and sends a message to your configured channel.

## 📁 Example Message in Discord
```markdown
**PR opened**: [Add login feature](https://github.com/user/repo/pull/123) by `johndoe`
```
## 🔧 .env Configuration
```env
DISCORD_BOT_TOKEN=your_discord_bot_token
DISCORD_CHANNEL_ID=your_channel_id
```
## 🛠 Deployment Notes
- Make sure port 5000 is open for incoming GitHub requests.

- Set up your GitHub repo to send webhooks to http://<your-aws-ip>:5000/webhook.

- Use a process manager like pm2 or systemd to run the bot persistently.
