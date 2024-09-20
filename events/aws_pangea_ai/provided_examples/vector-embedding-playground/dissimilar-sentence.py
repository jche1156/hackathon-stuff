import numpy as np
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity

client = OpenAI()


# Function to convert embeddings to numpy arrays for vector operations
def get_embedding_as_np(text, model="text-embedding-3-large"):
    text = text.replace("\n", " ")
    return np.array(client.embeddings.create(input=[text], model=model).data[0].embedding)

# Example analogy: king - man + woman ≈ queen
embedding1 = get_embedding_as_np("The stock market crashed yesterday.")
embedding2 = get_embedding_as_np("My favorite color is blue.")

# Calculate similarity between the resulting vector and the "queen" embedding
similarity = cosine_similarity([embedding1], [embedding2])[0][0]
print(f"Cosine similarity: {similarity}")
