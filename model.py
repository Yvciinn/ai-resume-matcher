import re
import nltk
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))
custom_stopwords = {
    "work", "experience", "job", "role", "responsibilities",
    "tasks", "candidate", "required", "looking", "seeking"
}

stop_words = set(stopwords.words('english')).union(custom_stopwords)

embed_model = SentenceTransformer('all-MiniLM-L6-v2')


def clean_text(text: str) -> str:
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z0-9+.# ]', ' ', text)
    words = [w for w in text.split() if w not in stop_words]
    return " ".join(words)


def _encode(texts: list) -> np.ndarray:
    return embed_model.encode(
        texts,
        batch_size=64,
        show_progress_bar=False,
        convert_to_numpy=True,
    ).astype('float32')


def find_top_jobs(resume_text: str, job_df: pd.DataFrame, top_n: int = 5):
    job_df = job_df.dropna(subset=['title', 'description']).reset_index(drop=True)

    if len(job_df) == 0:
        print("WARNING: job_df is empty after dropna.")
        return []

    texts = (job_df['title'] + " " + job_df['description']).tolist()
    cleaned = [clean_text(t) for t in texts]
    job_embs = _encode(cleaned)

    resume_emb = _encode([clean_text(resume_text)])
    scores = cosine_similarity(resume_emb, job_embs)[0]

    top_indices = scores.argsort()[::-1][:top_n]
    return [
        (str(job_df.iloc[i]['title']), float(scores[i]))
        for i in top_indices
    ]
