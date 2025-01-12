import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ResumeMatcher:
    def __init__(self, resume_path):
        self.nlp = spacy.load('en_core_web_sm')
        with open(resume_path, 'r') as file:
            self.resume_text = file.read()

    def preprocess(self, text):
        doc = self.nlp(text)
        tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
        return ' '.join(tokens)

    def match(self, job_description):
        resume_processed = self.preprocess(self.resume_text)
        job_description_processed = self.preprocess(job_description)

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([resume_processed, job_description_processed])
        similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        return similarity_score
