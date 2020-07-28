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
            print(synonym.upper() + ' already in database')
            exit()
    # If synonym is not in table, add word and synonym
    print('Adding synonym for ' + word.upper() + ' to database')
    cur.execute('''INSERT INTO SYNONYMS (word, synonym)
                    VALUES (?, ?)''', (w, s))
    conn.commit()
# Return true if at least 10 synonyms in database, false if not
def inSyn(word):
    tenSyn = False
    count = 0
    existing = cur.execute('''SELECT * FROM SYNONYMS''')
    for row in existing:
        if str(row[0]) == word:
            count += 1
    # Set tenSyn to True if there are 10 or more synonyms
    if count >= 10:
        tenSyn = True
        print('Already 10 synonyms for ' + word.upper() + ' in database')
    else:
        print('Less than 10 synonyms for ' + word.upper() + ' in database')
    return tenSyn
# Return random synonym for word from database
def getSyn(word):
    existing = cur.execute('''SELECT * FROM SYNONYMS WHERE word = ? ORDER BY random()''', (word,))
    print('Retrieved synonym for ' + word.upper() + ' from database')
    for row in existing:
        random = row[1]
    return random


# Add word and definition to DEFINITIONS table
def addDef(word, definition):
    w = str(word)
    d = str(definition)
    existing = cur.execute('''SELECT * FROM DEFINITIONS''')
    for row in existing:
        if str(row[1]) == d:
            print(definition.upper() + ' already in database')
            exit()
    print('Adding definition for ' + word + ' to database')
    cur.execute('''INSERT INTO DEFINITIONS (word, definition)
                    VALUES (?, ?)''', (w, d))
    conn.commit()
# Return true if definition in database, false if not
def inDef(word):
    existing = cur.execute('''SELECT * FROM DEFINITIONS''')
    for row in existing:
        if str(row[0]) == word:
            print('Definition for ' + word.upper() + ' in database')
            return True
        else:
            print('No definition for ' + word.upper() + ' in database')
    return False
# Return definition for word from database
def getDef(word):
    existing = cur.execute('''SELECT * FROM DEFINITIONS WHERE word = ?''', (word,))
    print('Retrieved definition for ' + word.upper() + ' from database')
    for row in existing:
        response = row[1]
    return response





# Add word and rhyme to RHYMES table
def addEx(word, example):
    w = str(word)
    e = str(example)
    existing = cur.execute('''SELECT * FROM EXAMPLES''')
    for row in existing:
        if str(row[1]) == e:
            print(example.upper() + ' already in database')
            exit()
    # If synonym is not in table, add word and synonym
    print('Adding example for ' + word.upper() + ' to database')
    cur.execute('''INSERT INTO EXAMPLES (word, example)
                    VALUES (?, ?)''', (w, e))
    conn.commit()
# Return true if ta lesat 10 examples in database, false if not
def inEx(word):
    tenEx = False
    count = 0
    existing = cur.execute('''SELECT * FROM EXAMPLES''')
    for row in existing:
        if str(row[0]) == word:
            count += 1
    if count >= 10:
        tenEx = True
        print('Already 10 examples for ' + word.upper() + ' in database')
    else:
        print('Less than 10 examples for ' + word.upper() + ' in database')
    return tenEx
# Return random example for word from database
def getEx(word):
    existing = cur.execute('''SELECT * FROM EXAMPLES WHERE word = ? ORDER BY random()''', (word,))
    print('Retrieved example for ' + word.upper() + ' from database')
    for row in existing:
        random = row[1]
    return random


conn.commit()
