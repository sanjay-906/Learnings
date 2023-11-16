import numpy as np
import matplotlib.pyplot as plt
import random
import time
bins= 70
array= [x for x in range(1,bins+1)]
random.shuffle(array)
array= np.array(array)
x= np.arange(0,bins,1)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

def quickSort(array, low, high):

    if low < high:
        plt.bar(list(range(1,bins+1)),array)
        plt.pause(0.001)
        plt.clf()
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
        plt.bar(list(range(1,bins+1)),array)
        plt.pause(0.001)
        plt.clf()

start_time = time.time()
quickSort(array, 0, len(array)-1)
print("Program execution time:", (time.time() - start_time))
plt.show()
