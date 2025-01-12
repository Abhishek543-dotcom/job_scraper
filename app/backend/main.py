from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)

# Sample job data
jobs = [
    {
        "title": "Software Engineer",
        "company": "TechCorp",
        "location": "San Francisco, CA",
        "match": "High",
        "applicationLink": "https://techcorp.com/careers/software-engineer"
    },
    {
        "title": "Data Scientist",
        "company": "DataCo",
        "location": "New York, NY",
        "match": "Moderate",
        "applicationLink": "https://dataco.com/careers/data-scientist"
    },
    {
        "title": "Product Manager",
        "company": "ProductInc",
        "location": "Seattle, WA",
        "match": "Low",
        "applicationLink": "https://productinc.com/careers/product-manager"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)
