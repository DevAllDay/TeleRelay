#telerelay.py
from discord import Webhook, RequestsWebhookAdapter, File
from telethon import TelegramClient, events, utils
import requests
import logging
import json

logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M',level=logging.INFO)
logger = logging.getLogger("telerelay")

with open("config.json") as config:
    config = json.load(config)
try:
	phone = config["tg"]["phone_num"]
	api_id = config["tg"]["app_id"]
	api_hash = config["tg"]["app_hash"]
	channelIds = config["tg"]["telegram_ids"]
	webhook = Webhook.partial(config["discord"]["webhook_id"], config["discord"]["webhook_token"], adapter=RequestsWebhookAdapter())
except:
	logger.error("There seems to be something wrong with the config!")
	
client = TelegramClient(phone, api_id, api_hash).start(phone)    

@client.on(events.NewMessage(chats=channelIds))
async def msg_handler(event):
    sender = await event.get_sender()
    name = utils.get_display_name(sender)
    msg = event.message.message

    logger.info(f"Message arrived from {name}\nMessage: {msg}")

    date_ = event.message.date.strftime("%m-%d-%Y %H:%M:%S")
    formattedMessage = f"`{name}\n[{date_}]`: {msg}"
    
    if event.message.media != None:
        try:
            fileName = await client.download_media(message=event.message.media)
            webhook.send(formattedMessage,file=File(fileName))
        except Exception as e:
            logger.error("Something happened while sending the relay message containing media\n{e}")
    else:
        try:
            webhook.send(formattedMessage)
        except Exception as e:
            logger.error("Something happened while sending the relay message\n{e}")
    
with client:
    client.run_until_disconnected()


