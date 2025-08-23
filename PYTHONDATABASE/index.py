

import mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "root"
)

mytob = mydb.cursor()
mytob.execute("CREATE DATABASE tobDB")

