# Vector Embeddings Playground

In this repo we use OpenAI's text embeddings API to understand how we can use vector similarities to identify similar text inputs.

A text embedding is just a vector representation of text data. In this repo, we use OpenAI's `text-embedding-3-large` to demonstrate properties of text embedding models.

## Setup
Install Packages
```
pip install -r requirements.txt
```

Add OpenAI API key to your environment. Get a key from [here](https://platform.openai.com/api-keys)
```
export OPENAI_API_KEY=<OPENAI_API_KEY>
```

## See examples:
* [vector-embedding.py](./vector-embedding.py) - Shows you what a text embedding looks like in vector form.
* [similar-sentence.py](./similar-sentence.py) - Create text embeddings of 2 similar sentences and calculates the cosine similarities (AKA how close 2 vectors are to each other; i.e. how similar are 2 sentences). In this case the similarity value will be closer to 1 instead of 0 since the 2 input sentences have great similarity.
* [dissimilar-sentence.py](./dissimilar-sentence.py) - Create text embeddings of 2 similar sentences and calculates the cosine similarities (AKA how close 2 vectors are to each other; i.e. how similar are 2 sentences). In this case the similarity value will be closer to 0 instead of 1 since the 2 input sentences have little to no similarity.
* [king-queen.py](./king-queen.py) - Shows how elaborately text embeddings are able to capture meanings of sentences. In here we take a sentence about a king subtract it from a sentance about a man and add it to a sentance about a woman. Here we can see that the final sentance is greatly similar to a sentance about a queen in vector form.