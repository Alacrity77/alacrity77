import sqlite3
import csv
from flask import Flask, render_template
import pandas as pd

## made a connection to the Database
connectionToDB = sqlite3.connect("CarbsPerFoodPrototype.db")
## use cursor will execute the SQL queries/Fetch ETC
cursor = connectionToDB.cursor()


## Makes a table in the database with name, carbs, as our columns
cursor.execute("CREATE TABLE IF NOT EXISTS foods(name, carbs)")

csvFile = "//RS-Cloud/RS-Shared/Adam/Coding/carbFolder/food.csv"


## reads and inserts, and commits all food into DB
with open(csvFile, "r") as file:
    reader = csv.reader(file)
    for i in reader:
        cursor.execute("INSERT INTO foods VALUES(?, ?)", i)
connectionToDB.commit()
