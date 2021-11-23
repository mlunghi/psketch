import json

if __name__ == "__main__":
    with open("synonyms.txt", "r") as f1, open("concatenated.json", "r") as f2:
        mapping = {"get": ["acquire", "obtain"], "use": ["utilize", "apply"]}
        lines = f1.readlines()
        synonyms = {}
        for line in lines:
            tokens = line.split()
            synonyms[tokens[0]] = [tokens[i] for i in range(1, len(tokens))]
        
        obj = json.load(f2)
        embeddings = {("acquire", "utilize"): {}, ("acquire", "apply"): {}, ("obtain", "utilize"): {}, ("obtain", "apply"): {}}
        for subtask, embedding in obj.items():
            tokens = subtask.split("_")
            for value in mapping[tokens[0]]:
                synonym_embedding = synonyms[value] + embedding[len(embedding)//2:]
                for combination in embeddings.keys():
                    if value in combination:
                        embeddings[combination][subtask+"/"+value+"_"+tokens[1]] = synonym_embedding

        for i, embedding in enumerate(list(embeddings.keys())):
            with open("synonyms_{}.json".format(i), "w") as fout:
                json.dump(embeddings[embedding], fout)

