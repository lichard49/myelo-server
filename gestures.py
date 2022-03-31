import numpy as np
import matplotlib.pyplot as plt
import sys
import os

from classification import parse_file, resample

# file = sys.argv[1]
# data = parse_file(file)

dir = 'data/toma_sitting_discrete' 
# dir = sys.argv[1] 

for file in os.listdir(dir):
    print(file)

gesture_list = ['index', 'middle', 'ring', 'pinky', 'fist', 'open', 'inwards', 'outwards', 'downwards', 'upwards', 'spiderman', 'swipe', 'dial', 'clockwise', 'counterclockwise']

by_gesture = {}
by_set = {}
dataset = {}

for i, file in os.listdir(dir):
    gesture = gesture_list[int(i%len(gesture_list))]
    set_num = int(i // len(gesture_list))
    data = parse_file(file)

    if gesture not in by_gesture:
        by_gesture[gesture] = []
    by_gesture[gesture].append(file)
    if set_num not in by_set:
        by_set[set_num] = []
    by_set[set_num].append(file)
    dataset[file] = data

# resample
dataset = resample(dataset)


train_index = [0, 1, 2, 3, 4, 5, 6, 7, 8]
test_index = [9, 10, 11, 12]