# DictionaryBot
This project was created to provide dictionary functionality within Discord servers in the form of an automated bot. Using the [WordsAPI](https://www.wordsapi.com/) and [World Clock API](http://worldclockapi.com/), the program web scrapes live JSON data to respond to user commands. To utilize this bot's features, please see **Setup** and **Commands**.

*Note: .env file is not included in repository and must be created by user*
## Requirements
Python 3
## Setup
1. Download *bot.py* and *timer.py*
2. Follow on-screen instructions at [WorldClockAPI](http://worldclockapi.com/) to create custom API key
3. Record custom API key
4. Go to Discord Developer Portal [WordsAPI](https://discord.com/developers/applications) and create a new application/bot
5. Record personal Discord token for your bot
6. Create a .env file with the following lines: 
```
      DISCORD_TOKEN={your_token}
      API_KEY={your_key}
```      
7. Invite bot to Discord server
8. Run *bot.py* and enjoy your new bot!
## Commands
- **"usage"**: displays all bot commands 
- **"def WORD"**: outputs most common dictionary definition of WORD
- **"syn WORD"**: outputs list of synonyms of WORD
- **"rhy WORD SYLLABLES(optional)"**: outputs random rhyme of WORD that has the corresponding SYLLABLES
- **"ex WORD"**: outputs an example of WORD
- **"rand"**: outputs random word
## Contact
Created by [Aiden Szeto](https://www.linkedin.com/in/aidenszeto/) - feel free to contact me!
