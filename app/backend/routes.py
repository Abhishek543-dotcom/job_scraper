from flask import Blueprint, request, jsonify
from .models import db, Job, Application

api = Blueprint('api', __name__)

@api.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([job.to_dict() for job in jobs])

@api.route('/jobs', methods=['POST'])
def create_job():
    data = request.json
    new_job = Job(
        title=data['title'],
        company=data['company'],
        location=data['location'],
        description=data['description'],
        requirements=data['requirements'],
        application_link=data['application_link'],
        hr_email=data.get('hr_email')
    )
    db.session.add(new_job)
    db.session.commit()
    return jsonify(new_job.to_dict()), 201

@api.route('/applications', methods=['POST'])
def create_application():
    data = request.json
    new_application = Application(
        job_id=data['job_id'],
        status=data.get('status', 'pending')
    )
    db.session.add(new_application)
    db.session.commit()
    return jsonify(new_application.to_dict()), 201

@api.route('/applications/<int:application_id>', methods=['PUT'])
def update_application(application_id):
    application = Application.query.get_or_404(application_id)
    data = request.json
    application.status = data.get('status', application.status)
    db.session.commit()
    return jsonify(application.to_dict())

@api.route('/applications/<int:application_id>', methods=['DELETE'])
def delete_application(application_id):
    application = Application.query.get_or_404(application_id)
    db.session.delete(application)
    db.session.commit()
    return '', 204
