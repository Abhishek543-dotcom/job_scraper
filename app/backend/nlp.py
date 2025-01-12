import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the pre-trained NLP model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

def calculate_similarity(job_description, resume_text):
    # Preprocess the texts
    job_description = preprocess_text(job_description)
    resume_text = preprocess_text(resume_text)
    
    # Vectorize the texts
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([job_description, resume_text])
    
    # Calculate cosine similarity
    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return similarity_score

def match_resume_with_jobs(resume_text, job_list):
    matched_jobs = []
    for job in job_list:
        similarity_score = calculate_similarity(job['description'], resume_text)
        job['similarity_score'] = similarity_score
        matched_jobs.append(job)
    
    # Sort jobs by similarity score
    matched_jobs.sort(key=lambda x: x['similarity_score'], reverse=True)
    return matched_jobs
