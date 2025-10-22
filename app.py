from flask import Flask, request
from instabot import Bot
import os

app = Flask(__name__)

# ---------- CONFIGURATION ----------
# Use environment variables for safety
INSTAGRAM_USERNAME = os.getenv("INSTA_USERNAME", "mk_test_xx_1")
INSTAGRAM_PASSWORD = os.getenv("INSTA_PASSWORD", "mahabbat@2008")
TARGET_USER = os.getenv("INSTA_TARGET", "mk__mahabbat")

# Optional: protect the /follow route with a secret key
SECRET_KEY = os.getenv("FOLLOW_SECRET", "mysecret123")
# -----------------------------------

@app.route('/')
def home():
    return "✅ Instabot Web Service is running!"

@app.route('/follow')
def follow_user():
    # Check secret key
    key = request.args.get("key")
    if key != SECRET_KEY:
        return "🚫 Unauthorized access"

    try:
        bot = Bot()  # Create bot inside route
        bot.login(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)
        bot.follow(TARGET_USER)
        bot.logout()
        return f"🎯 Followed user: {TARGET_USER}"
    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == "__main__":
    # Render requires using the PORT environment variable
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
