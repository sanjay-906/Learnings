import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(real, img, max_iter):
  c= complex(real, img)
  z= 0.0j
  for i in range(max_iter):
    z= z*z+ c
    if(z.real*z.real + z.imag*z.imag)>=4:
      return 1
  return max_iter

columns= 2000
rows= 2000

for k in range(50):
  result= np.zeros([rows,columns])
  for i, real in enumerate(np.linspace(-2,1,num= rows)):
    for j, img in enumerate(np.linspace(-1,1,num= columns)):
      result[i,j]= mandelbrot(real,img, k)
  plt.figure(figsize=(16,16),dpi= 100)
  plt.imshow(result, cmap='gist_heat') #afmhot #gist_earth
  plt.xlabel('Real')
  plt.ylabel('Img')
  plt.savefig('{}.png'.format(k),dpi=100)
  plt.show()
