from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
DATABASE ='form.db'

with sqlite3.connect(DATABASE) as conn:
    c =conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS form
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                first name TEXT,
                last name TEXT,
                email TEXT
                phone INTEGER)''')


@app.route("/", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        firstname  = request.form['firstname']
        lastname = request.form['lastname']
        email =request.form['email']
        phone = request.form['phone']

        with sqlite3.connect(DATABASE) as conn:
            c =conn.cursor()
            c.execute("INSERT INTO form (Firstname, Lastname, email, phone) VALUES (), (), (), ()" (firstname, lastname, email, phone))

    with sqlite3.connect(DATABASE) as conn:
            c =conn.cursor()
            c.execute('SELECT * FROM form')
            form = c.fetchall()
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()