import sqlite3

conn = sqlite3.connect('cards.db')
c = conn.cursor()

with open('insert_cards.txt') as file:
    c.execute(file.read().replace(r"\'", "`"))

conn.commit()
conn.close()
