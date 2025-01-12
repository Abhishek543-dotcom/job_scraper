import torch
from transformers import BertTokenizer, BertModel

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def get_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', max_length=512, truncation=True)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().detach().numpy()

def match_resume_to_job(resume, job_description):
    resume_embedding = get_embedding(resume)
    job_embedding = get_embedding(job_description)
    similarity = torch.cosine_similarity(torch.tensor(resume_embedding), torch.tensor(job_embedding), dim=0)
    return similarity.item()
