# Personal Discord Bot

This bot was created to make usage of personal servers easier.
> Keep in mind that this bot was designed ONLY for usage on a private personal servers.

Functions:
- Fields for notes
- Saving messages
- Task Manager
- Schedule of completed tasks (productivity chart)
- Task Reminder
- The Eisenhower Matrix
- Protected channels (with a white list)
- Saving content from the internet
- Copying web pages
- Search for text on images
- FIGfont generator

## Installation

1. Install Python 3.9 or newer.
```
sudo apt install python3.9
```

2. Install the packages.
```
pip install discord.py
pip install --upgrade discord-components
```

3. Create an Application on Discord Developers portal:
https://discord.com/developers/applications
And Invite the bot you created to your Discord server.

4. Configure your bot.
Paste your Application token to token.yaml file.
Change setting in config.yaml as you want.

5. Start your bot and set it up by command in your Discord server.

You are ready to go!

#####Bot commands:
<br/>
```!setup``` - install all channels and categoried to start working with the bot.<br/>
```!reset``` - delete all the channels and categories that were created by a bot.<br/>
```!hard_reset``` - delete all the channels and categories on the server.<br/>

