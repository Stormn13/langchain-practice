from langchain_huggingface import HuggingFaceEmbeddings

embendding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = 'hello is the capital of india'

vector = embendding.embed_query(text)

print(vector)