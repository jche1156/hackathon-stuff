import numpy as np
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity

client = OpenAI()


# Function to convert embeddings to numpy arrays for vector operations
def get_embedding_as_np(text, model="text-embedding-3-large"):
    text = text.replace("\n", " ")
    return np.array(client.embeddings.create(input=[text], model=model).data[0].embedding)

# get vector embedding for this sentence
emb_king_sentence = get_embedding_as_np("The king is ruling the kingdom.")

# print embedding
print(emb_king_sentence)
# print vector size
print(emb_king_sentence.shape)
