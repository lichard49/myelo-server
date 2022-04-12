import matplotlib.pyplot as plt
import numpy as np
import sys

file = sys.argv[1]

samples = []
millis = []
data1 = []
data2 = []
data3 = []
data4 = []
with open(file, 'r') as file_handler:
    for line in file_handler:
        line = line.strip()
        if len(line) > 0:
            line_parts = line.split(',')
            samples.append(float(line_parts[0]))
            millis.append(float(line_parts[1]))
            data1.append(float(line_parts[2]))
            data2.append(float(line_parts[3]))
            data3.append(float(line_parts[4]))
            data4.append(float(line_parts[5]))

start = millis[0]
prev = start
index = 0

# time_passed = millis[-1] - start
# print("time_passed", time_passed)

samps = []

for _ in range(19):
    start = millis[index]
    prev_ind = index
    for i, m in enumerate(millis):
        if m - start >= 1000 and prev - start < 1000:
            index = i
            print(start, m, i)
        prev = m

    print(samples[index] - samples[0])
    samps.append(samples[index] - samples[prev_ind])

print("avg", np.mean(samps))

# f, ax = plt.subplots(2, sharex=True)
# ax[0].plot(data1)
# ax[1].plot(data2)
# ax[2].plot(data1)
# ax[3].plot(data2)
# plt.show()

plt.figure()
plt.plot(data1)
plt.plot(data2)
plt.plot(data3)
plt.plot(data4)
plt.show()

