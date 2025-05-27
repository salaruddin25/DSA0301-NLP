import math
from collections import Counter, defaultdict

# Sample corpus of documents
documents = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "cats and dogs are animals",
    "the quick brown fox jumps over the lazy dog"
]

# Preprocessing: Tokenize and lowercase
def tokenize(text):
    return text.lower().split()

# Step 1: Compute Term Frequency (TF)
def compute_tf(doc_tokens):
    tf = Counter(doc_tokens)
    total_terms = len(doc_tokens)
    for term in tf:
        tf[term] /= total_terms
    return tf

# Step 2: Compute Inverse Document Frequency (IDF)
def compute_idf(docs_tokens):
    N = len(docs_tokens)
    idf = defaultdict(lambda: 0)
    for tokens in docs_tokens:
        unique_terms = set(tokens)
        for term in unique_terms:
            idf[term] += 1
    for term in idf:
        idf[term] = math.log(N / idf[term])
    return idf

# Step 3: Compute TF-IDF vectors for documents
def compute_tfidf(tf, idf):
    tfidf = {}
    for term, val in tf.items():
        tfidf[term] = val * idf.get(term, 0)
    return tfidf

# Step 4: Cosine similarity between two vectors
def cosine_similarity(vec1, vec2):
    common = set(vec1.keys()) & set(vec2.keys())
    num = sum(vec1[t] * vec2[t] for t in common)
    denom1 = math.sqrt(sum(v ** 2 for v in vec1.values()))
    denom2 = math.sqrt(sum(v ** 2 for v in vec2.values()))
    if denom1 == 0 or denom2 == 0:
        return 0.0
    return num / (denom1 * denom2)

# Build TF-IDF model
docs_tokens = [tokenize(doc) for doc in documents]
doc_tfs = [compute_tf(tokens) for tokens in docs_tokens]
idf = compute_idf(docs_tokens)
doc_tfidfs = [compute_tfidf(tf, idf) for tf in doc_tfs]

# Query processing
def search(query, top_k=3):
    query_tokens = tokenize(query)
    query_tf = compute_tf(query_tokens)
    query_tfidf = compute_tfidf(query_tf, idf)

    # Rank documents by similarity
    scores = []
    for i, doc_vec in enumerate(doc_tfidfs):
        sim = cosine_similarity(query_tfidf, doc_vec)
        scores.append((i, sim))

    ranked = sorted(scores, key=lambda x: x[1], reverse=True)
    print(f"\nTop {top_k} results for query: \"{query}\"")
    for i, score in ranked[:top_k]:
        print(f"Doc #{i + 1} (score: {score:.4f}): {documents[i]}")

# Run the search
if __name__ == "__main__":
    while True:
        q = input("\nEnter your search query (or type 'exit'): ")
        if q.lower() == "exit":
            break
        search(q)
