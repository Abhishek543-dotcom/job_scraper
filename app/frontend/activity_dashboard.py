from flask import Flask, render_template, request, jsonify
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

@app.route('/submit_application', methods=['POST'])
def submit_application():
    data = request.json
    conn = get_db_connection()
    conn.execute('INSERT INTO applications (job_id, status) VALUES (?, ?)', (data['job_id'], 'pending'))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

@app.route('/update_application', methods=['POST'])
def update_application():
    data = request.json
    conn = get_db_connection()
    conn.execute('UPDATE applications SET status = ? WHERE id = ?', (data['status'], data['id']))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
