import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import matplotlib.cm as cm
from numpy.random import random

data = defaultdict(list)
original_numbers = []
with open('rewards.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     i = 0
     for row in spamreader:

         if i == 0 or i == 2:
             i += 1
             continue

         if i == 1:
            original_numbers = row
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

counter = 0
for experiment in data.keys():
    x = []
    y = []
    counter += 1
    if counter == 1:
        for idx, type in enumerate(data[experiment]):
            row = type
            x += [1,2,3,4,5]
            y += [float(row[1])/float(original_numbers[2]), float(row[2])/float(original_numbers[3]), float(row[3])/float(original_numbers[4]), float(row[4])/float(original_numbers[5]), float(row[5])/float(original_numbers[6])]

        colors = cm.rainbow(np.linspace(0, 1, len(y)))
        i = 0
        legend_str = []

        for curr_y, c in zip(y, colors):
            f = plt.scatter(x[i], curr_y, color=c, label = curr_y)
            i += 1

        plt.title("Experiment " + str(counter) + ": " + str(experiment))
        classes = ["synonym", "related", "random", "noise", "most similar"]
        class_colours = ['#8A2BE2','#6495ED','#00FFFF', '#98FB98', '#FFA500']
        recs = []
        import matplotlib.patches as mpatches

        for i in range(0,len(class_colours)):
            recs.append(mpatches.Rectangle((0,0),1,1,fc=class_colours[i]))

        plt.legend(recs,classes,bbox_to_anchor=(1.1, 1.05))
        plt.ylim(0,1)
        plt.show()
    else:
        for idx, type in enumerate(data[experiment]):
            row = type
            x += [1,2,3,4,5]
            y += [float(row[1])/float(original_numbers[2]), float(row[2])/float(original_numbers[3]), float(row[3])/float(original_numbers[4]), float(row[4])/float(original_numbers[5]), float(row[5])/float(original_numbers[6])]

        colors = cm.rainbow(np.linspace(0, 1, len(y)))
        i = 0
        legend_str = []
        if 0 in y:
            print("TRUE")

        for curr_y, c in zip(y, colors):
            f = plt.scatter(x[i], curr_y, color=c, label = curr_y)
            i += 1

        plt.title("Experiment " + str(counter) + ": " + str(experiment))
        classes = ["synonym", "related", "random", "noise", "most similar", "antonym"]
        class_colours = ['#8A2BE2','#6495ED','#00FFFF', '#98FB98', '#FFA500', 'red']
        recs = []
        import matplotlib.patches as mpatches

        for i in range(0,len(class_colours)):
            recs.append(mpatches.Rectangle((0,0),1,1,fc=class_colours[i]))

        plt.legend(recs,classes,bbox_to_anchor=(1.1, 1.05))
        plt.ylim(0,1)
        plt.show()
