from langchain_huggingface import HuggingFaceEmbeddings

from sklearn.metrics.pairwise import cosine_similarity

embedding = HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')

docs = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills",
    "Sachin Tendulkar, also know as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record breaking double centuries.",
    "Jasprit Bumra is an Indian fast bowler known for his unorthodox action and yorkers"
]

query = "tell me about virat kohli"

doc_embeddings = embedding.embed_documents(docs)
query_embeddings = embedding.embed_query(query)

print(cosine_similarity([query_embeddings], doc_embeddings))