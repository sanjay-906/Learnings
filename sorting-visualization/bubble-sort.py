import numpy as np
import matplotlib.pyplot as plt
import random
import time
bins= 15
lst= [x for x in range(1,bins+1)]
random.shuffle(lst)
lst= np.array(lst)
x= np.arange(0,bins,1)
n= len(lst)

start_time = time.time()
for i in range(n):
    for j in range(0,n-i-1):
        plt.bar(x,lst)
        plt.pause(0.001)
        plt.clf()

        if lst[j]>lst[j+1]:
            lst[j], lst[j+1]= lst[j+1], lst[j]
print("Program execution time:", (time.time() - start_time))
plt.show()
