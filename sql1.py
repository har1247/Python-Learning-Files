import sqlite3
import urllib.request, urllib.parse, urllib.error
import ssl

conn = sqlite3.connect("organizationdb.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

filename = input("Enter a file name: ")
if len(filename) < 1:
    filename="mbox.txt"
fh = open(filename)

for line in fh:
    if line.startswith("From: "):
        pieces = line.split()
        email = pieces[1].split('@')
        org = email[1]
        cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
        row = cur.fetchone()

        if row is None:
            cur.execute('INSERT INTO Counts (org , count) VALUES (?,1)', (org,))
        else:
            cur.execute('UPDATE Counts SET count= count + 1 WHERE org=?', (org,))
        conn.commit()

output = 'SELECT * FROM Counts ORDER BY count desc'

for row in cur.execute(output):
    print(str(row[0]), row[1])
cur.close()
