import nltk
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

nltk.download('punkt')

from nltk.tokenize import sent_tokenize

def evaluate_coherence(text):
    sentences = sent_tokenize(text)
    if len(sentences) < 2:
        return 1.0

    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(sentences)
    similarities = []

    for i in range(len(embeddings) - 1):
        sim = cosine_similarity([embeddings[i]], [embeddings[i + 1]])[0][0]
        similarities.append(sim)

    coherence_score = np.mean(similarities)
    return coherence_score

if __name__ == "__main__":
    sample_text = """
    Artificial Intelligence is transforming the world. Machines can now understand natural language. This progress helps industries automate tasks. 
    However, ethical concerns must be addressed. Climate change is a growing threat to our environment.
    """
    score = evaluate_coherence(sample_text)
    print(f"Coherence Score: {score:.4f}")
