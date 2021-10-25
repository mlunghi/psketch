#!/bin/bash

#SBATCH -p gpu --gres=gpu:2
#SBATCH -n 1
#SBATCH --mem=64G
#SBATCH -t 3:00:00

module load cuda
module load anaconda/2020.02
source /gpfs/runtime/opt/anaconda/2020.02/etc/profile.d/conda.sh
conda activate csci2951x

python main.py