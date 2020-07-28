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
    sUp = s.upper()
    # If synonym is already in table, exit
    existing = cur.execute('''SELECT * FROM SYNONYMS''')
    for row in existing:
        if str(row[1]) == s:
            print(sUp + ' already in database')
            exit()
    # If synonym is not in table, add word and synonym
    print('Adding ' + sUp + ' to database')
    cur.execute('''INSERT INTO SYNONYMS (word, synonym)
                    VALUES (?, ?)''', (w, s))
    conn.commit()
# Return true if 10 synonyms in database, false if not
def inSyn(word):
    tenSyn = False
    count = 0
    wUp = str(word.upper())
    existing = cur.execute('''SELECT * FROM SYNONYMS''')
    for row in existing:
        if str(row[0]) == word:
            count += 1
    # Set tenSyn to True if there are 10 or more synonyms
    if count >= 10:
        tenSyn = True
        print('Already 10 synonyms for ' + wUp + ' in database')
    else:
        print('Less than 10 synonyms for ' + wUp + ' in database')
    return tenSyn
# Return random synonym for word from database
def getSyn(word):
    wUp = str(word.upper())
    existing = cur.execute('''SELECT * FROM SYNONYMS WHERE word = ? ORDER BY random()''', (word,))
    print('Retrieved ' + wUp + ' from database')
    for row in existing:
        random = row[1]
    return random


# Add word and definition to DEFINITIONS table
def addDef(word, definition):
    w = str(word)
    d = str(definition)
    dUp = d.upper()
    existing = cur.execute('''SELECT * FROM DEFINITIONS''')
    for row in existing:
        if str(row[1]) == d:
            print(dUp + ' already in database')
            exit()
    print('Adding ' + dUp + ' to database')
    cur.execute('''INSERT INTO DEFINITIONS (word, definition)
                    VALUES (?, ?)''', (w, d))
    conn.commit()
# Return true if definition in database, false if not
def inDef(word):
    wUp = str(word.upper())
    existing = cur.execute('''SELECT * FROM DEFINITIONS''')
    for row in existing:
        if str(row[0]) == word:
            print('Definition for ' + wUp + ' in database')
            return True
        else:
            print('No definition for ' + wUp + ' in database')
    return False
# Return definition for word from database
def getDef(word):
    wUp = str(word.upper())
    existing = cur.execute('''SELECT * FROM DEFINITIONS WHERE word = ?''', (word,))
    print('Retrieved definition for ' + wUp + ' from database')
    for row in existing:
        response = row[1]
    return response


# Add word, rhyme, and syllbale count to RHYMES table
def addRhy(word, rhyme, syl):
    w = str(word)
    r = str(rhyme)
    rUp = r.upper()
    s = int(syl)
    existing = cur.execute('''SELECT * FROM RHYMES''')
    for row in existing:
        if str(row[1]) == r:
            print(rUp + ' already in database')
            exit()
    print('Adding ' + rUp + ' to database')
    cur.execute('''INSERT INTO RHYMES (word, rhyme, syllables)
                    VALUES (?, ?, ?)''', (w, d, s))
    conn.commit()
# Return true if 10 rhymes with corresponding syllables in database, false if not
def inRhy(word, syl):
    tenRhy = False
    count = 0
    wUp = str(word.upper())
    # When syllable count not provided
    if syl == None:
        existing = cur.execute('''SELECT * FROM RHYMES''')
    # When syllable count is provided
    else:
        s = int(syl)
        existing = cur.execute('''SELECT * FROM RHYMES WHERE syllables = ?''', (s,))
    for row in existing:
        if str(row[0]) == word:
            count += 1
    if count >= 10:
        tenRhy = True
        print('Already 10 rhymes for ' + wUp + ' in database')
    else:
        print('Less than 10 rhymes for ' + wUp + ' in database')    
    return tenRhy


# Add word and rhyme to RHYMES table
def addEx(word, example):
    w = str(word)
    e = str(example)
    eUp = e.upper()
    existing = cur.execute('''SELECT * FROM EXAMPLES''')
    for row in existing:
        if str(row[1]) == e:
            print(eUp + ' already in database')
            exit()
    # If synonym is not in table, add word and synonym
    print('Adding "' + eUp + '" to database')
    cur.execute('''INSERT INTO EXAMPLES (word, example)
                    VALUES (?, ?)''', (w, e))
    conn.commit()
# Return true if 10 examples in database, false if not
def inEx(word):
    tenEx = False
    count = 0
    wUp = str(word.upper())
    existing = cur.execute('''SELECT * FROM EXAMPLES''')
    for row in existing:
        if str(row[0]) == word:
            count += 1
    if count >= 10:
        tenEx = True
        print('Already 10 examples for ' + wUp + ' in database')
    else:
        print('Less than 10 examples for ' + wUp + ' in database')
    return tenEx
# Return random example for word from database
def getEx(word):
    wUp = str(word.upper())
    existing = cur.execute('''SELECT * FROM EXAMPLES WHERE word = ? ORDER BY random()''', (word,))
    print('Retrieved example for ' + wUp + ' from database')
    for row in existing:
        random = row[1]
    return random


conn.commit()
