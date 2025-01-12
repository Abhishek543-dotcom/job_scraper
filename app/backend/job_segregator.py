from app.backend.resume_matcher import ResumeMatcher

class JobSegregator:
    def __init__(self, resume_path):
        self.resume_matcher = ResumeMatcher(resume_path)
        self.high_match = []
        self.moderate_match = []
        self.low_match = []

    def segregate_jobs(self, job_list):
        for job in job_list:
            similarity_score = self.resume_matcher.match(job['description'])
            if similarity_score >= 0.8:
                self.high_match.append(job)
            elif similarity_score >= 0.5:
                self.moderate_match.append(job)
            else:
                self.low_match.append(job)

    def get_high_match(self):
        return self.high_match

    def get_moderate_match(self):
        return self.moderate_match

    def get_low_match(self):
        return self.low_match
