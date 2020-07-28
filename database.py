import sqlite3
import random
from sys import exit

# Connect to database
conn = sqlite3.connect('Dictionary.db')
cur = conn.cursor()
print("Successfully connected to Dictionary.db")


# Add word and synonym to SYNONYMS table
def addSyn(word, synonym):
    # If synonym is already in table, exit
    existing = cur.execute('SELECT synonym FROM SYNONYMS')
    for row in existing:
        if str(row) == synonym:
            print('Synonym already in database')
            exit()
    # If synonym is not in SYNONYMS table, add word and synonym
    conn.execute('''INSERT INTO SYNONYMS (word, synonym) VALUES (?, ?)''', (word, synonym))

# Check if synonyms is already in database
def inSyn(word):
    # Return true if at least 10 synonyms is in database, false if not
    existing = cur.execute('SELECT word FROM SYNONYMS')
    for row in existing:
        if str(row) == word:
            print('Synonym already in database')
            return True
    print('Synonym not in database')
    return False

# Return random synonym for word from database
def getSyn(word):
    existing = cur.execute('SELECT synonym FROM SYNONYMS WHERE word = ?', (word))
    print('Retrieved synonym from database')
    return random.choice(existing)


conn.commit()
