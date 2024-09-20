import numpy as np
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity

client = OpenAI()


# Function to convert embeddings to numpy arrays for vector operations
def get_embedding_as_np(text, model="text-embedding-3-large"):
    text = text.replace("\n", " ")
    return np.array(client.embeddings.create(input=[text], model=model).data[0].embedding)

# Get vector embeddings of similar sentences.
embedding1 = get_embedding_as_np("I enjoy eating pizza for dinner.")
embedding2 = get_embedding_as_np("I love having pizza for my evening meal.")

# Calculate similarity between the resulting vector and the "queen" embedding
similarity = cosine_similarity([embedding1], [embedding2])[0][0]
print(f"Cosine similarity: {similarity}")
