import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import matplotlib.cm as cm
from numpy.random import random

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

    colors = cm.rainbow(np.linspace(0, 1, len(y)))
    i = 0
    legend_str = []

    for curr_y, c in zip(y, colors):
        f = plt.scatter(x[i], curr_y, color=c, label = curr_y)
        # plt.legend((f),
        #        ("Type 1: Purple", "Type 2: Blue", "Type 3: Turquoise", "Type 4: Green", "Type 5: Orange"),
        #        scatterpoints=1,
        #        loc='lower left',
        #        ncol=3,
        #        fontsize=8)
        i += 1
    # colors = ['p', 'b', 't', 'g', 'o']
    plt.title("Experiment: " + str(experiment))
    classes = ["1", "2", "3", "4", "5"]
    class_colours = ['#8A2BE2','#6495ED','#00FFFF', '#98FB98', '#FFA500']
    recs = []
    import matplotlib.patches as mpatches

    for i in range(0,len(class_colours)):
        recs.append(mpatches.Rectangle((0,0),1,1,fc=class_colours[i]))
    plt.legend(recs,classes,loc=4)


    plt.show()
