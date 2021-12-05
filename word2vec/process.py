import gensim.downloader
glove_vectors = gensim.downloader.load('glove-wiki-gigaword-100')

import os
import json
from collections import defaultdict

import numpy as np

EMBEDDING_DIMENSION = 100

def create_token_embeddings():
    """
    Given tokens.json creates token_embeddings.json
    """
    for directory in ("verbs", "nouns", "verbs+nouns"):
        embeddings = {}
        metrics = defaultdict(lambda: {})
        with open(os.path.join(directory, "tokens.json"), "r") as f:
            tokens = json.load(f)
            for original, transformed in tokens.items():
                if transformed is None:
                    embeddings[original] = glove_vectors[original].tolist()
                else:
                    for i in range(len(transformed)):
                        embeddings[transformed[i]] = glove_vectors[transformed[i]].tolist()
                        metrics[original][transformed[i]] = float(glove_vectors.similarity(original, transformed[i]))
        with open(os.path.join(directory, "token_embeddings.json"), "w") as f:
            json.dump(embeddings, f)
        with open(os.path.join(directory, "metrics.json"), "w") as f:
            json.dump(metrics, f)

def _noise(directory, subtask_embeddings, original_subtask_embeddings):
    if directory == "verbs":
        start, end = 0, 100
    elif directory == "nouns":
        start, end = 100, 200
    elif directory == "verbs+nouns":
        start, end = 0, 200
    for original_tokens, embedding in original_subtask_embeddings.items():
        subtask_embedding = []
        for i in range(len(embedding)):
            if start < i < end:
                subtask_embedding.append(np.random.normal())
            else:
                subtask_embedding.append(embedding[i])
        subtask_embeddings["_".join(original_tokens)+"/"+"_".join(original_tokens)] = subtask_embedding

def create_subtask_embeddings():
    """
    Given tokens_embeddings.json creates subtask_embeddings.json
    """
    with open("original/subtask_embeddings.json", "r") as f:
        original_subtask_embeddings = json.load(f)
        original_subtask_embeddings = {tuple(k.split("_")): list(map(float, v)) for k, v in original_subtask_embeddings.items()}
        
    for directory in ("verbs", "nouns", "verbs+nouns"):
        with open(os.path.join(directory, "token_embeddings.json"), "r") as f_embeddings, open(os.path.join(directory, "tokens.json"), "r") as f_tokens:
            embeddings = json.load(f_embeddings)
            tokens_mapping = json.load(f_tokens)
            for transformation in (("most_similar", 0), ("synonym", 1), ("related", 2), ("random", 3), ("antonym", 4), ("noise", None)):
                subtask_embeddings = {}
                if transformation[0] == "noise":
                    _noise(directory, subtask_embeddings, original_subtask_embeddings)
                else:         
                    for original_tokens, embedding in original_subtask_embeddings.items():
                        tokens = []
                        subtask_embedding = []
                        for i in range(len(original_tokens)):
                            if tokens_mapping[original_tokens[i]] is not None and transformation[1] < len(tokens_mapping[original_tokens[i]]):
                                token = tokens_mapping[original_tokens[i]][transformation[1]]
                                tokens.append(token)
                                subtask_embedding += embeddings[token]
                            else:
                                tokens.append(original_tokens[i])
                                subtask_embedding += embedding[100*i:100*i+EMBEDDING_DIMENSION]
                        subtask_embeddings["_".join(original_tokens)+"/"+"_".join(tokens)] = subtask_embedding

                with open(os.path.join(directory, "subtask_embeddings", "subtask_embeddings_" + transformation[0].upper() + ".json"), "w") as f:
                    json.dump(subtask_embeddings, f)

if __name__ == "__main__":
    create_token_embeddings()
    create_subtask_embeddings()