# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "X-URL-Uploader",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    Config.AUTH_USERS.add(958850850)
    app.run()


from pyrogram import Client 
from config import API_ID, API_HASH, BOT_TOKEN, FORCE_SUB, PORT
from aiohttp import web
from route import web_server

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="X-URL-Uploader",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username 
        self.force_channel = FORCE_SUB
        if FORCE_SUB:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB)                  
                self.invitelink = link
            except Exception as e:
                print(e)
                print("Make Sure Bot admin in force sub channel")             
                self.force_channel = None
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"       
        await web.TCPSite(app, bind_address, PORT).start()     
        print(f"{me.first_name} ЁЭЪВЁЭЪГЁЭЩ░ЁЭЪБЁЭЪГЁЭЩ┤ЁЭЩ│ тЪбя╕ПтЪбя╕ПтЪбя╕П")
      

    async def stop(self, *args):
        await super().stop()      
        print("Bot Stopped")
       

bot=Bot()
bot.run()
