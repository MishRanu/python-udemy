import sqlite3

conn = sqlite3.connect("contacts.sqlite")
cursor = conn.cursor()
name = input("Please enter the name to query: \n").strip("\n")

select_query = "SELECT * FROM contacts WHERE name = ?"
cursor.execute(select_query, (name,))

for name, phone, email in cursor:
    print(name + "\t")
    print(str(phone) + "\t")
    print(email + "\t")

cursor.close()
conn.close()