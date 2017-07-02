'''
I use this file to test the library on heroku.
'''

import os

from microsoftbotframework.msbot import MsBot
from tasks import *

if __name__ == "__main__":
    bot = MsBot(port=int(os.environ['PORT']), debug=True)
    bot.add_process(respond_to_conversation_update)
    bot.add_process(echo_response_async)
    bot.add_process(echo_response)
    bot.run()
