from .nlp_utils import match_resume_to_job

def categorize_jobs(jobs, resume, threshold_high=0.8, threshold_moderate=0.5):
    high_match = []
    moderate_match = []
    low_match = []

    for job in jobs:
        similarity = match_resume_to_job(resume, job['description'])
        if similarity >= threshold_high:
            high_match.append(job)
        elif similarity >= threshold_moderate:
            moderate_match.append(job)
        else:
            low_match.append(job)

    return high_match, moderate_match, low_match
