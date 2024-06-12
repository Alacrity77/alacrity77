from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
DATABASE = 'CarbsPerFoodPrototype.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    return db

@app.route('/')
def index():
    ICR_Value = request.args.get('ICR', '')
    search_term = request.args.get('search', '')
    foods = []

    db = get_db()
    cursor = db.cursor()

    try:
        ICR_Value = float(ICR_Value)
    except ValueError:
        ICR_Value = None

    if search_term:
        cursor.execute("SELECT name, carbs FROM foods WHERE name LIKE ?", ('%' + search_term + '%',))
        result = cursor.fetchall()

        for row in result:
            name, carbs = row
            reqInsulin = None
            if carbs and ICR_Value:
                try:
                    reqInsulin = round(float(carbs) / ICR_Value, 2)
                except ZeroDivisionError:
                    reqInsulin = 0
            foods.append((name, carbs, reqInsulin))
    db.close()
    return render_template('index.html', foods=foods, search_term=search_term, ICR_VALUE=ICR_Value)

if __name__ == '__main__':
    app.run(debug=True)
