import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
data = defaultdict(list)
with open('rewards.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     i = 0
     for row in spamreader:

         if i == 0:
             i += 1
             continue

         experiment = row[0]
         type = row[1]
         r1 = row[2]
         r2 = row[3]
         r3 = row[4]
         r4 = row[5]
         r5 = row[6]
         data[experiment].append([type,r1,r2,r3,r4,r5])

for experiment in data.keys():
    x = []
    y = []
    for idx, type in enumerate(data[experiment]):
        row = type
        x += [1,2,3,4,5]
        y += [float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5])]
    print(y)
    plt.scatter(x, y)
    plt.title("Experiment: " + str(experiment))
    plt.show()
