from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'job_applications.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS job_applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_title TEXT,
                company TEXT,
                location TEXT,
                application_status TEXT,
                email_status TEXT,
                date_applied TEXT
            )
        ''')
        conn.commit()

@app.route('/')
def index():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM job_applications')
        applications = cursor.fetchall()
    return render_template('index.html', applications=applications)

@app.route('/add_application', methods=['POST'])
def add_application():
    job_title = request.form['job_title']
    company = request.form['company']
    location = request.form['location']
    application_status = request.form['application_status']
    email_status = request.form['email_status']
    date_applied = request.form['date_applied']

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO job_applications (job_title, company, location, application_status, email_status, date_applied)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (job_title, company, location, application_status, email_status, date_applied))
        conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
