from flask import Flask
from instabot import Bot

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Instabot Web Service is running!"

@app.route('/follow')
def follow_user():
    # ⚠️ Educational only — do not hardcode real passwords in production
    username = "mk_test_xx_1"
    password = "mahabbat@2008"
    target = "mk__mahabbat"

    bot = Bot()
    try:
        bot.login(username=username, password=password)
        bot.follow(target)
        bot.logout()
        return f"🎯 Followed user: {target}"
    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
