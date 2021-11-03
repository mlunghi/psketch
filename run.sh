#!/bin/bash

#SBATCH -n 8
#SBATCH --mem=64G
#SBATCH -t 48:00:00

module load anaconda/2020.02
source /gpfs/runtime/opt/anaconda/2020.02/etc/profile.d/conda.sh
conda activate csci2951x

python main.py