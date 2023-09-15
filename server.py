import sys
from gunicorn.app.wsgiapp import run
from threading import Thread
import telepot
import os, time

def send_to_tg():
    bot = telepot.Bot(os.getenv("prodipto_bot_token"))
    chat_id = os.getenv("error_message_chat_id")
    while True:
        bot.sendMessage(chat_id, "Message was sent from cyclic!")
        time.sleep(1*60)

if __name__ == '__main__':
    sys.argv = "gunicorn --bind 0.0.0.0:5151 app:app".split()
    Thread(target=send_to_tg).start()
    sys.exit(run())
