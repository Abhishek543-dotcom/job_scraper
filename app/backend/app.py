from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_applications.db'
db = SQLAlchemy(app)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    match = db.Column(db.String(50), nullable=False)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    job_title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pending')

@app.route('/')
def index():
    jobs = Job.query.all()
    applications = Application.query.all()
    return render_template('index.html', jobs=jobs, applications=applications)

@app.route('/submit_application', methods=['POST'])
def submit_application():
    job_id = request.json['job_id']
    job = Job.query.get(job_id)
    if job:
        new_application = Application(job_id=job_id, job_title=job.title, company=job.company)
        db.session.add(new_application)
        db.session.commit()
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error', 'message': 'Job not found'})

@app.route('/update_application', methods=['POST'])
def update_application():
    application_id = request.json['id']
    status = request.json['status']
    application = Application.query.get(application_id)
    if application:
        application.status = status
        db.session.commit()
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error', 'message': 'Application not found'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
