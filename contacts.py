import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts(name TEST, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES ('Tim', 6545678, 'tim@gmail.com')")
db.execute("INSERT INTO contacts VALUES ('Anurag', 9845678, 'anurag@gmail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

print(cursor.fetchall())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("="*20)

db.commit()
cursor.close()
db.close()