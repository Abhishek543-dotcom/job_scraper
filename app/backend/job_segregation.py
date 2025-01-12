from app.backend.resume_matching import ResumeMatcher

class JobSegregator:
    def __init__(self, resume_text):
        self.resume_text = resume_text
        self.resume_matcher = ResumeMatcher(resume_text)

    def segregate_jobs(self, job_listings):
        high_match = []
        moderate_match = []
        low_match = []

        for job in job_listings:
            similarity_score = self.resume_matcher.match_resume_to_job(job['description'])
            if similarity_score >= 0.8:
                high_match.append(job)
            elif similarity_score >= 0.5:
                moderate_match.append(job)
            else:
                low_match.append(job)

        return {
            'high_match': high_match,
            'moderate_match': moderate_match,
            'low_match': low_match
        }

# Example usage
if __name__ == "__main__":
    resume_text = "Experienced software engineer with a strong background in Python and web development."
    job_listings = [
        {
            'title': 'Software Engineer',
            'company': 'TechCorp',
            'location': 'San Francisco, CA',
            'description': 'We are looking for a software engineer with experience in Python and web development to join our team.'
        },
        {
            'title': 'Data Scientist',
            'company': 'DataCo',
            'location': 'New York, NY',
            'description': 'We are looking for a data scientist with experience in machine learning and data analysis.'
        },
        {
            'title': 'Frontend Developer',
            'company': 'WebDevCo',
            'location': 'Remote',
            'description': 'We are looking for a frontend developer with experience in React and JavaScript.'
        }
    ]

    job_segregator = JobSegregator(resume_text)
    segregated_jobs = job_segregator.segregate_jobs(job_listings)
    print(f"High Match: {segregated_jobs['high_match']}")
    print(f"Moderate Match: {segregated_jobs['moderate_match']}")
    print(f"Low Match: {segregated_jobs['low_match']}")
