import matplotlib.pyplot as plt
import sys

file = sys.argv[1]

data1 = []
data2 = []
with open(file, 'r') as file_handler:
    for line in file_handler:
        line = line.strip()
        if len(line) > 0:
            line_parts = line.split(',')
            data1.append(float(line_parts[0]))
            data2.append(float(line_parts[1]))

f, ax = plt.subplots(2, sharex=True)
ax[0].plot(data1)
ax[1].plot(data2)
plt.show()
