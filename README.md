# DictionaryBot
This project was created to provide dictionary functionality within Discord servers in the form of an automated bot. Using the [WordsAPI](https://www.wordsapi.com/) and [World Clock API](http://worldclockapi.com/), the program web scrapes live JSON data to respond to user commands. For more information about utilizing this bot's features, please see [**Setup**](https://github.com/aidenszeto/DictionaryBot/blob/master/README.md#setup) and [**Commands**](https://github.com/aidenszeto/DictionaryBot/blob/master/README.md#commands).

*Note: The .env file containing the Discord Token and API Key is not included in repository and must be created by user.*
## Setup
1. Download *bot.py* and *timer.py*
2. Follow on-screen instructions at [WorldClockAPI](http://worldclockapi.com/) to create custom API key
3. Record your custom API Key
4. Go to Discord Developer Portal [WordsAPI](https://discord.com/developers/applications) and create a new application/bot
5. Record the Discord Token that corresponds to your bot
6. Create a .env file in the same directory as *bot.py* and *timer.py* with the following lines: 
```
      DISCORD_TOKEN={your_token}
      API_KEY={your_key}
```      
7. Invite bot to Discord server
8. Run *bot.py* and enjoy your new bot!

*Click [here](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-python) for more information regarding bot setup*
## Commands
- **usage**: displays all bot commands 
- **def WORD**: outputs most common dictionary definition of WORD
- **syn WORD**: outputs list of synonyms of WORD
- **rhy WORD SYLLABLES(optional)**: outputs random rhyme of WORD that has the corresponding SYLLABLES
- **ex WORD**: outputs an example of WORD
- **rand**: outputs random word
## Database
The current *Dictionary.db* is a sample database that will be populated as the progrma continues to scrape data and will change depending on the bot's usage. In order to optimize bot performance and limit API calls, after 10 differing **syn**, **rhy**, or **ex** commands for each word, the application will only output data from the database, rather than the [WordsAPI](https://www.wordsapi.com/). Following the 10 commands, no new API calls will be made.

To disable the database and force the bot to scrape web data in all scenarios, simply remove ```import database.py``` from *bot.py*, along with the remaining *database.py* methods. This, in effect, will prevent the bot from using stored data.
## Contact
Created by [Aiden Szeto](https://www.linkedin.com/in/aidenszeto/) - feel free to contact me!
