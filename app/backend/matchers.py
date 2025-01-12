import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the pre-trained NLP model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

def match_resume_to_job(resume, job_description):
    resume = preprocess_text(resume)
    job_description = preprocess_text(job_description)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume, job_description])
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return cosine_sim

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
