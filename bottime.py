import sys
import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
# Enter your ID in next function's argument
bot = telepot.Bot('<EnterHereYourUserCode>')
bot.message_loop(handle)
print 'I am listening...'

while 1:
    time.sleep(10)
# EOF
