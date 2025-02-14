#!/bin/bash

#SBATCH -n 1
#SBATCH --mem=4G
#SBATCH -t 3:00:00

module load anaconda/2020.02
source /gpfs/runtime/opt/anaconda/2020.02/etc/profile.d/conda.sh
conda activate csci2951x

python main.py --synonyms $embedding