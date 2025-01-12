from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'job_applications.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    jobs = conn.execute('SELECT * FROM jobs').fetchall()
    applications = conn.execute('SELECT * FROM applications').fetchall()
    conn.close()
    return render_template('index.html', jobs=jobs, applications=applications)

@app.route('/add_job', methods=['POST'])
def add_job():
    job_title = request.form['job_title']
    company = request.form['company']
    location = request.form['location']
    description = request.form['description']
    application_link = request.form['application_link']
    hr_email = request.form['hr_email']
    
    conn = get_db_connection()
    conn.execute('INSERT INTO jobs (job_title, company, location, description, application_link, hr_email) VALUES (?, ?, ?, ?, ?, ?)',
                 (job_title, company, location, description, application_link, hr_email))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/add_application', methods=['POST'])
def add_application():
    job_id = request.form['job_id']
    status = request.form['status']
    
    conn = get_db_connection()
    conn.execute('INSERT INTO applications (job_id, status) VALUES (?, ?)',
                 (job_id, status))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
