from instabot import Bot

# ⚠️ EDUCATIONAL EXAMPLE — Do NOT use real credentials in public repos!
username = "mk_test_xx_1"
password = "mahabbat@2008"
target = "mk__mahabbat"

bot = Bot()
bot.login(username=username, password=password)
bot.follow(target)
bot.logout()
