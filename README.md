# TeleRelay

Welcome to TeleRelay, A Telegram -> Discord relay with the use of Discord.py rewrite and Telethon.
It will watch for updates on the IDs provided in the config file, the event will be triggered whenver a message is sent, fairly easy to setup.

To run the script to relay messages and media over to your discord channel, we need to install the essential modules so this is able to run.
```
pip install -U telethon 
pip install -U discord.py
```
After you've done that, you need git installed to clone this repo to your local desktop. 
Clone the repo like so
```
git clone https://github.com/DevAllDay/TeleRelay.git
```
Before you run `relay.py`, we'll need to setup the `config.json` file - 
To start off, you need to head to https://my.telegram.org and create a app which returns `app_id` and `app_hash`.
Now we can input these values into the config -

`tg`

`app_id` - Integer

`api_hash` - String

`phone_num` - String, phone number used to sign in telegram

`telegram_ids` - List of channel IDs you want to relay to Discord

`discord`

`webhook_id` - Integer, can be obtained from the first part of the webhook URL 

`webhook_token` - String, can be obtained from the second part of the webhook URL

Save the config now (CTRL+S) and make sure you named the config `config.json` otherwise `relay.py` won't be able to read it.

You might be wondering, how do i obtain channel IDs to input into the config file? Hmmm, well i've created another file in this repo to assist you into obtaining the IDs, its easy to use, you just run it after saving the config, 

```
Type 1 for Groups/DMs/Chats etc. OR Type 2 for Username/Channel/Groups ID searching using tag: 1
Telegram Entity ID Grabber
-------------------------------------------------------------
0. Telegram
1. Testing
2. 123
3. Discord
-------------------------------------------------------------
Which channel/group/DM do you want the ID of? Use the number! 2
123940094
```
After you run `getID.py`, you'll see the same as above, it'll ask you for input to retrieve the ID from your dialogs or you can enter the username and it will fetch the ID for you and return it, but above we chose option 1 which was to retrieve my dialogs and then chose `123` channel to get the ID. You've got the ID from here now, all you need to do is insert it into the List in `config.json` and save it. 
You can now run `relay.py` which should run smoothly :) 
