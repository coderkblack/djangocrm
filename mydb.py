import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zarak1kenp@chi",
    auth_plugin='mysql_native_password'
)

#prepare cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE elderco")
print("All Done!")

#python manage.py migrate
#winpty python manage.py createsuperuser