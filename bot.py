import discord
from discord.ext import commands
from flask import Flask, request
from dotenv import load_dotenv
import threading
import os

load_dotenv()

# Load from environment (recommended) or paste your bot token
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Your Discord channel ID where you want threads/messages
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))  # replace with your channel ID

# Set up bot intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
app = Flask(__name__)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@app.route("/webhook", methods=["POST"])
def github_webhook():
    data = request.json
    action = data.get("action")
    pr = data.get("pull_request", {})
    title = pr.get("title")
    url = pr.get("html_url")
    user = pr.get("user", {}).get("login")

    message = f"**PR {action}**: [{title}]({url}) by `{user}`"

    # Run async bot action from Flask
    bot.loop.create_task(send_to_discord(message))
    return {"status": "ok"}, 200

async def send_to_discord(message):
    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        print("Channel not found.")
        return

    # Optionally create or reuse a thread
    thread = await channel.create_thread(name="GitHub PR Updates", type=discord.ChannelType.public_thread)
    await thread.send(message)

# Run Flask server and Discord bot
def run_flask():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    bot.run(TOKEN)
