import telebot
import requests


URL_AUTH = "https://developers.lingvolive.com/api/v1.1/authenticate"
URL_TRANSLATE = "https://developers.lingvolive.com/api/v1/Minicard"
KEY = "OWFlNjZjYjEtNzE2OS00ZTA4LWJlMjEtMjBmMWQ1Yzk1MDRjOmMxZmY5MDMwMjcxNDRiNDdiZDc1MzdmMWJiYzczYmM3"
TOKEN = '5250513223:AAE7roliwVV11F9XvEVeIZyixmJmUZBW7Tc'

headers_auth = {"Authorization": "Basic " +KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)

bot = telebot.TeleBot(TOKEN)
if auth.status_code == 200:
    token = auth.text

@bot.message_handler(content_types=["text"])
def test(message):
    word = message.text
    headers_translate = {
        "Authorization": "Bearer " + token
    }
    params = {
        "text": word,
        "srcLang": 1033,
        "dstLang": 1049
    }
    r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
    res = r.json()
    bot.send_message(message.chat.id,res["Translation"] ["Translation"])
bot.polling(none_stop=True)