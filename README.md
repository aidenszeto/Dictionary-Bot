# DictionaryBot
This project was created to provide dictionary functionality within Discord servers in the form of an automated bot. Using the WordsAPI (https://www.wordsapi.com/) and World Clock API (http://worldclockapi.com/), the program web scrapes live JSON data to respond to user commands. To utilize this bot's features, a user must invite the bot to a custom Discord server. Afterwards, "usage" may be typed into any channel within the server to display all of the DictionaryBot's commands.
## Setup
1. Download *bot.py* and *timer.py*
2. Follow on-screen instructions at [WorldClockAPI](http://worldclockapi.com/) to create custom API key
3. Record custom API key
4. Go to Discord Developer Portal [WordsAPI](https://discord.com/developers/applications) and create a new application/bot
5. Record personal Discord token for your bot
6. Create a .env file with the following lines: 
      **DISCORD_TOKEN={your_token}** and **API_KEY={your_key}**
7. Invite bot to Discord server
8. Run *bot.py* and enjoy your new bot!
## Contact
Created by [Aiden Szeto](https://www.linkedin.com/in/aidenszeto/) - feel free to contact me!
