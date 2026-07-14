import sqlite3 as sql
import os
from collections import Counter

DB = "database.db"
print(os.path.abspath(DB))
conn = sql.connect(DB, timeout=30)
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS user")

gamelist = []
slope_rating = 0
course_rating = 0.0
handicap = 0
score = 0
totalscore = 0
differential = 0
mostusedclub = "undefined"
first_n = "Corey"
last_n = "Beard"
dob = "2009-06-11"
club = "Shooters Hill"
email = "cbd@outlook.com"

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS user (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     firstname TEXT NOT NULL,
#     lastname TEXT NOT NULL,
#     DateOfBirth TEXT NOT NULL,
#     Handicap FLOAT,
#     club_name TEXT NOT NULL,
#     email TEXT NOT NULL
# )
#
# """)
# print("Table made")
#
# cursor.execute("""
# INSERT INTO user (firstname, lastname, DateOfBirth, Handicap, club_name, email)
# VALUES (?, ?, ?, ?, ?, ?)
# """, (first_n, last_n, dob, handicap, club, email))
#
# cursor.execute("SELECT club_name FROM user WHERE id = ?", (1,))
# result = cursor.fetchone()
# club_name = result[0]
# if club_name == "Shooters Hill":
#     slope_rating = 122
#     course_rating = 69.2
# print("Row inserted successfully.")
# conn.commit()
#
# cursor.execute("DROP TABLE IF EXISTS game")
#
def gamecreation():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS game (
        HoleNumber INTEGER PRIMARY KEY AUTOINCREMENT,
        PAR Integer NOT NULL,
        DISTANCE FLOAT NOT NULL,
        Shots Integer NOT NULL,
        Clubs_used TEXT NOT NULL,
        Putter_count INTEGER NOT NULL
    )
    
    """)
    conn.commit()

    print("Table made")
    for i in range(1, 11):
        PAR = int(input("Enter Par number: "))
        DIST = int(input("Enter distance from tee: "))
        Shot = int(input("Enter number of shots taken: "))
        Clubs_usd = input("Enter which Clubs used: ")
        Putter_coun = int(input("Enter how many times was putter used? "))
        cursor.execute("""
        INSERT INTO game (PAR, DISTANCE, Shots, Clubs_used, Putter_count)
        VALUES (?, ?, ?, ?, ?)
        """, (PAR, DIST, Shot, Clubs_usd, Putter_coun))
        print("Row inserted successfully.")
        totalscore = totalscore + Shot
        differential = ((Shot - course_rating) * 113) / slope_rating
        gamelist.append(differential)
        conn.commit()

    # Get all clubs used from the table
    cursor.execute("SELECT Clubs_used FROM game")
    clubs = cursor.fetchall()

    # Simplify list for changes
    club_list = [club[0].lower() for club in clubs]

    # Remove putter since its always used
    club_list = [club for club in club_list if club != "putter"]

    # Find most common club
    if club_list:
        mostusedclub = Counter(club_list).most_common(1)[0][0]
    else:
        mostusedclub = None

    print("Most used club (excluding putter):", mostusedclub)
    # Take lowest 10 values
    lowest_10 = sorted(gamelist)[:10]

    # Calculate handicap
    handicap = sum(lowest_10) * 0.96

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print(cursor.fetchall())

    print("Tables in DB:")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    for table in cursor.fetchall():
        print(table)

    cursor.execute("DROP TABLE IF EXISTS stats")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stats (
        GameN INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        Handicap FLOAT,
        mostused TEXT NOT NULL
    )
    
    """)
    print("Table made")
    cursor.execute("""
    INSERT INTO stats (firstname, lastname, Handicap, mostused)
    VALUES (?, ?, ?, ?)
    """, (first_n, last_n, handicap, mostusedclub))
    conn.commit()

    conn.close()