import sqlite3
from sys import exit

# Connect to database
conn = sqlite3.connect('Dictionary.db')
cur = conn.cursor()
print("Successfully connected to Dictionary.db")


# Add word and synonym to SYNONYMS table
def addSyn(word, synonym):
    w = str(word)
    s = str(synonym)
    # If synonym is already in table, exit
    existing = cur.execute('''SELECT * FROM SYNONYMS''')
    for row in existing:
        if str(row[1]) == s:
            print(synonym + ' already in database')
            exit()
    # If synonym is not in table, add word and synonym
    print('Adding synonym for ' + word + ' to database')
    cur.execute('''INSERT INTO SYNONYMS (word, synonym)
                    VALUES (?, ?)''', (w, s))
    conn.commit()

# Check if synonyms is already in database
def inSyn(word):
    # Return true if at least 5 synonyms is in database, false if not
    existing = cur.execute('''SELECT * FROM SYNONYMS''')
    for row in existing:
        if str(row[0]) == word:
            print('5 synonyms for ' + word + ' already in database')
            return True
    print('Less than 5 synonyms for ' + word + ' in database')
    return False

# Return random synonym for word from database
def getSyn(word):
    existing = cur.execute('''SELECT * FROM SYNONYMS WHERE word = ? ORDER BY random()''', (word,))
    print('Retrieved synonym for ' + word + ' from database')
    for row in existing:
        random = row[1]
    return random


conn.commit()
