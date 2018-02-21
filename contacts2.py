import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = 'anotherupdate@update.com'
# phone = 6545678
phone = input("Please enter the phone number \n")
# update_sql = "UPDATE contacts SET email = '{}' WHERE contacts.phone={}".format(new_email, phone)

update_sql = "UPDATE contacts SET email = ? WHERE contacts.phone = ?"
print(update_sql)
update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
print("{} rows updated".format(update_cursor.rowcount))
update_cursor.connection.commit()

update_cursor.close()

for name, phone, email in db.execute("SELECT * From contacts"):
    print(name)
    print(phone)
    print(email)
    print("="*20)

db.close()