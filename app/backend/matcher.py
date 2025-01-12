import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class JobMatcher:
    def __init__(self, resume_text):
        self.resume_text = resume_text
        self.nlp = spacy.load('en_core_web_sm')
        self.vectorizer = TfidfVectorizer()

    def preprocess_text(self, text):
        doc = self.nlp(text)
        tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
        return ' '.join(tokens)

    def match_jobs(self, job_listings):
        resume_vector = self.vectorizer.fit_transform([self.preprocess_text(self.resume_text)])
        job_vectors = self.vectorizer.transform([self.preprocess_text(job['description']) for job in job_listings])
        similarities = cosine_similarity(resume_vector, job_vectors).flatten()

        for i, job in enumerate(job_listings):
            job['similarity'] = similarities[i]

        return job_listings

    def segregate_jobs(self, job_listings, thresholds):
        high_match = [job for job in job_listings if job['similarity'] >= thresholds['high']]
        moderate_match = [job for job in job_listings if thresholds['high'] > job['similarity'] >= thresholds['moderate']]
        low_match = [job for job in job_listings if job['similarity'] < thresholds['moderate']]

        return {
            'high_match': high_match,
            'moderate_match': moderate_match,
            'low_match': low_match
        }
