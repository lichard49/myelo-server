import numpy as np
import pandas as pd

from tslearn.preprocessing import TimeSeriesResampler

def parse_file(filename, norm=True, samples=True, millis=True, data_streams=4):
    data = {}
    if samples is True:
        data["samples"] = []
    if millis is True:
        data["millis"] = []
    for d in np.arange(data_streams):
        data["data"+str(d)] = []

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) > 0:
                components = line.split(',')
                for i, k in enumerate(data):
                    print(i, k)
                    data[k].append(float(components[i]))
                    # implement a way to make sure this doesn't mess up based on input vs parameters
    if norm:
        for d in data:
            if d != "samples" and d != "millis":
                data[d] = normalize(data[d])
    
    return data

# not sure how to scale this based on input params...
def normalize(signal, outmin=-1, outmax=1): 
    in_range = (np.max(signal) - np.min(signal)) / 2
    in_middle = np.max(signal) - in_range
    in_avg = np.mean(signal)
    temp = signal - in_middle
    return temp / in_range


def resample(dataset):
    longest = 0
    for f in dataset:
        if len(dataset[f]["data0"]) > longest:
            longest = len(dataset[f]["data0"])
    for f in dataset:
        for d in dataset[f]:
            dataset[f][d] = TimeSeriesResampler(sz=longest).fit_transform(dataset[f][d])
    return dataset