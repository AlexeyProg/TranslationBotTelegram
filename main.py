import telebot
import requests


URL_AUTH = "https://developers.lingvolive.com/api/v1.1/authenticate"
URL_TRANSLATE = "https://developers.lingvolive.com/api/v1/Minicard"
KEY = ""
TOKEN = ''
text_help = "Для перевода слова с английского языка на русский просто введите необходимое слово"

headers_auth = {"Authorization": "Basic " +KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)

bot = telebot.TeleBot(TOKEN)
if auth.status_code == 200:
    token = auth.text

@bot.message_handler(content_types=["text"])
def test(message):
    word = message.text
    if word == "/help":
        bot.send_message(message.chat.id, text_help)
    else:
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
        try:
            tex = res["Translation"] ["Translation"]
        except:
            tex = "Не удалось найти такое слово"
        bot.send_message(message.chat.id, tex)

bot.polling(none_stop=True)