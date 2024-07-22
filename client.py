# Don't Remove Credit @TonyStark_Botz
# Join our Telegram Channel For Amazing Bot @TonyStark_Botz
# Ask Doubt on telegram @TonyStarkBotzXSupport

from info import *
from pyrogram import Client

class Bot(Client):   
    def __init__(self):
        super().__init__(   
           "tony-post-search-bot",
            api_id=API_ID,
            api_hash=API_HASH,           
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"})
    async def start(self):                        
        await super().start()  
        print("Bot Started 🔧 Powered By @TonyStark_Botz")   
    async def stop(self, *args):
        await super().stop()
