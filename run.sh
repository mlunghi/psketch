#!/bin/bash

#SBATCH -n 8
#SBATCH --mem=64G
#SBATCH -t 48:00:00

module load anaconda/2020.02
source /gpfs/runtime/opt/anaconda/2020.02/etc/profile.d/conda.sh
conda activate csci2951x

embeddings=( "word2vec/swap.json" "word2vec/synonyms_1.json" "word2vec/synonyms_2.json" "word2vec/synonyms_3.json" )
for i in "${embeddings[@]}"
do
    python main.py --synonyms $i
done