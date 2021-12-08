#!/bin/bash

prefix=( "word2vec/verbs/subtask_embeddings/subtask_embeddings_" "word2vec/nouns/subtask_embeddings/subtask_embeddings_" "word2vec/verbs+nouns/subtask_embeddings/subtask_embeddings_" )
suffix=( "MOST_SIMILAR.json" "SYNONYM.json" "RELATED.json" "RANDOM.json" "ANTONYM.json" "NOISE.json" )
for i in "${prefix[@]}"
do

for j in "${suffix[@]}"
do

sbatch --export=embedding="$i$j" run.sh

done

done