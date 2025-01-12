import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ResumeMatcher:
    def __init__(self, resume_text):
        self.resume_text = resume_text
        self.nlp = spacy.load("en_core_web_sm")

    def preprocess_text(self, text):
        doc = self.nlp(text)
        tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
        return " ".join(tokens)

    def match_resume_to_job(self, job_description):
        resume_processed = self.preprocess_text(self.resume_text)
        job_processed = self.preprocess_text(job_description)

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([resume_processed, job_processed])
        similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

        return similarity_score

# Example usage
if __name__ == "__main__":
    resume_text = "Experienced software engineer with a strong background in Python and web development."
    job_description = "We are looking for a software engineer with experience in Python and web development to join our team."

    resume_matcher = ResumeMatcher(resume_text)
    similarity_score = resume_matcher.match_resume_to_job(job_description)
    print(f"Similarity Score: {similarity_score}")
