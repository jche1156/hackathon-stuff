import numpy as np
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity

client = OpenAI()


# Function to convert embeddings to numpy arrays for vector operations
def get_embedding_as_np(text, model="text-embedding-3-large"):
    text = text.replace("\n", " ")
    return np.array(client.embeddings.create(input=[text], model=model).data[0].embedding)

# Example analogy: king - man + woman ≈ queen
emb_king_sentence = get_embedding_as_np("The king is ruling the kingdom.")
emb_queen_sentence = get_embedding_as_np("The queen is ruling the kingdom.")
emb_man_sentence = get_embedding_as_np("The man is working in the office.")
emb_woman_sentence = get_embedding_as_np("The woman is working in the office.")

# Perform the analogy operation (all vectors are now numpy arrays)
analogy_vector = emb_king_sentence - emb_man_sentence + emb_woman_sentence

# Calculate similarity between the resulting vector and the "queen" embedding
similarity = cosine_similarity([analogy_vector], [emb_queen_sentence])[0][0]
print(f"Cosine similarity between 'king - man + woman' and 'queen': {similarity}")
