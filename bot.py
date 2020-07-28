import os
import random
import discord
import urllib.request, urllib.parse, urllib.error
import json
import http.client
import re
import syllables
import timer, database
from sys import exit
from dotenv import load_dotenv


# Connect to Discord and load API key
load_dotenv()
KEY = os.getenv('API_KEY')
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


# Dm to welcome new server members
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


# Command responses
@client.event
async def on_message(message):
    # Ensure that bot responses are not taken as input
    if message.author == client.user:
        return

    # Initialize calls to 0 and curent to js['dayOfTheWeek']
    calls = 0
    current = timer.current()

    # Prints all possible commands
    commands = [
        "def WORD\n"
        "syn WORD\n"
        "rhy WORD\n"
        "ex WORD\n"
        "rand"
    ]
    if message.content.lower() == 'usage':
        response = ", ".join(commands)
        await message.channel.send(response)


    # Usage: def WORD
    # If usage is followed, use word API to return definition of WORD
    elif re.search('^def ', message.content.lower()):
        # If it is a new day, reset calls count to 0
        timer.check(current, calls)
        # Split input into 'def' and 'WORD' and assign variable to WORD
        input = message.content.lower().split()
        word = input[1]
        # Check if usage is followed
        if len(input) != 2:
            await message.channel.send("Usage: def WORD")
        else:
            # If word is already in db, set response to definition from db
            if database.inDef(word):
                response = str(database.getDef(word))
            # If word is not in db, set response to definition from API
            else:
                # Connect to word API with correct headers
                conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")
                headers = {
                    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
                    'x-rapidapi-key': KEY
                    }
                conn.request("GET", "/words/" + word + "/definitions", headers=headers)
                # Decode UTF8 response
                res = conn.getresponse()
                data = res.read().decode("utf-8")
                # Create JSON object from data
                try:
                    js = json.loads(data)
                except:
                    js = None
                # Check JSON object for errors (ie. invalid WORD)
                if not js or 'definitions' not in js:
                    message.channel.send('Definition not found')
                # Set response to definition from PI
                response = word + ': ' + js["definitions"][0]['definition']
                # Add word and synonym to database
                database.addDef(word, response)
            # Send response
            await message.channel.send(response)
            # Increment calls and set current to new js['dayOfTheWeek']
            calls += 1
            current = timer.current()
            # If call limit is reached, exit the bot
            if calls >= 2500:
                await message.channel.send("API limit has been reached")
                exit()


    # Usage: syn WORD
    # If usage is followed, use word API to return a synonym of WORD
    elif re.search('^syn ', message.content.lower()):
        # If it is a new day, reset calls count to 0
        timer.check(current, calls)
        # Split input into 'syn' and 'WORD' and assign variable to WORD
        input = message.content.lower().split()
        word = input[1]
        # Check if usage is followed
        if len(input) != 2:
            await message.channel.send("Usage: syn WORD")
        else:
            # If word is already in db, set response to synonym from db
            if database.inSyn(word):
                response = str(database.getSyn(word))
            # If word is not in db, set response to synonym from API
            else:
                # Connect to word API with correct headers
                conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")
                headers = {
                    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
                    'x-rapidapi-key': KEY
                    }
                conn.request("GET", "/words/" + word + "/synonyms", headers=headers)
                # Decode UTF8 response
                res = conn.getresponse()
                data = res.read().decode("utf-8")
                # Create JSON object from data
                try:
                    js = json.loads(data)
                except:
                    js = None
                # Check JSON object for errors (ie. invalid WORD)
                if not js or 'synonyms' not in js:
                    message.channel.send('Synonym not found')
                # Set response to random synonym from API
                synonyms = js["synonyms"]
                response = random.choice(synonyms)
                # Add word and synonym to database
                database.addSyn(word, response)
            # Send response
            await message.channel.send(response + " is a synonym of " + word)
            # Increment calls and set current to new js['dayOfTheWeek']
            calls += 1
            current = timer.current()
            # If call limit is reached, exit the bot
            if calls >= 2500:
                await message.channel.send("API limit has been reached")
                exit()


    # Usage: rhy WORD SYLLABLES(optional)
    # If usage is followed, use word API to return a rhyme of WORD
    elif re.search('^rhy ', message.content.lower()):
        # If it is a new day, reset calls count to 0
        timer.check(current, calls)
        # Split input into 'rhy' and 'WORD' and assign variable to WORD
        input = message.content.lower().split()
        word = input[1]
        # Check if usage is followed
        if len(input) != 2 and len(input) != 3:
            await message.channel.send("Usage: rhy WORD SYLLABLES(optional)")
        else:
            # Connect to word API with correct headers
            conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")
            headers = {
                'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
                'x-rapidapi-key': KEY
                }
            conn.request("GET", "/words/" + word + "/rhymes", headers=headers)
            # Decode UTF8 response
            res = conn.getresponse()
            data = res.read().decode("utf-8")
            # Create JSON object from data
            try:
                js = json.loads(data)
            except:
                js = None
            # Check JSON object for errors (ie. invalid WORD)
            if not js or 'rhymes' not in js:
                message.channel.send('Rhyme not found')
            # Create rhymes list
            rhymes = js["rhymes"]["all"]
            # If no syllable count is provided, output random rhyme
            if len(input) == 2:
                response = random.choice(rhymes)
                await message.channel.send(response + " rhymes with " + word)
            # If syllable count is provided, output rhyme with corresponding syllables
            elif len(input) == 3:
                sylin = int(input[2])
                # Create array of rhymes with syllable count that matches sylin
                matches = []
                for rhyme in rhymes:
                    if " " in rhyme or "-" in rhyme:
                        continue
                    # If syllable count matches sylin, add rhyme to matches array
                    if syllables.estimate(rhyme) == sylin:
                        matches.append(rhyme)
                # Print random corresponding rhyme if found
                if len(matches) == 0:
                    message.channel.send('Rhyme not found')
                else:
                    response = random.choice(matches)
                    await message.channel.send(response + " is a " + str(sylin) + " syllable word that rhymes with " + word)
        # Increment calls and set current to new js['dayOfTheWeek']
        calls += 1
        current = timer.current()
        # If call limit is reached, exit the bot
        if calls >= 2500:
            await message.channel.send("API limit has been reached")
            exit()

    # Usage: ex WORD
    # If usage is followed, use word API to return an example of WORD
    elif re.search('^ex ', message.content.lower()):
        # If it is a new day, reset calls count to 0
        timer.check(current, calls)
        # Split input into 'ex' and 'WORD' and assign variable to WORD
        input = message.content.lower().split()
        word = input[1]
        # Check if usage is followed
        if len(input) != 2:
            await message.channel.send("Usage: ex WORD")
        else:
            # If word is already in db, set response to example from db
            if database.inEx(word):
                response = str(database.getEx(word))
            # If word is not in db, set response to example from API
            else:
                # Connect to word API with correct headers
                conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")
                headers = {
                    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
                    'x-rapidapi-key': KEY
                    }
                conn.request("GET", "/words/" + word + "/examples", headers=headers)
                # Decode UTF8 response
                res = conn.getresponse()
                data = res.read().decode("utf-8")
                # Create JSON object from data
                try:
                    js = json.loads(data)
                except:
                    js = None
                # Check JSON object for errors (ie. invalid WORD)
                if not js or 'examples' not in js:
                    message.channel.send('Example not found')
                # Set response to random example from API
                examples = js["examples"]
                response = random.choice(examples)
                # Add word and synonym to database
                database.addEx(word, response)
            # Send response
            await message.channel.send("example: " + response)
            # Increment calls and set current to new js['dayOfTheWeek']
            calls += 1
            current = timer.current()
            # If call limit is reached, exit the bot
            if calls >= 2500:
                await message.channel.send("API limit has been reached")
                exit()


    # Usage: rand
    # If usage is followed, use word API to return a rhyme of WORD
    elif message.content.lower() == 'rand':
        # If it is a new day, reset calls count to 0
        timer.check(current, calls)
        # Connect to word API with correct headers
        conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")
        headers = {
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
            'x-rapidapi-key': KEY
            }
        conn.request("GET", "/words/?random=true", headers=headers)
        # Decode UTF8 response
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        # Create JSON object from data
        try:
            js = json.loads(data)
        except:
            js = None
        # Respond with random word
        word = js["word"]
        await message.channel.send(word)
        # Increment calls and set current to new js['dayOfTheWeek']
        calls += 1
        current = timer.current()
        # If call limit is reached, exit the bot
        if calls >= 2500:
            await message.channel.send("API limit has been reached")
            exit()


client.run(TOKEN)
