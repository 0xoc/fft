import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import scipy.signal
import math

def row_col_multi(row, col):
    lr = len(row)
    
    sum = 0

    for i in range(lr):
        sum += row[i] * col[i]
    
    return sum

def multi(mat, col):
    return [ row_col_multi(row, col) for row in mat ]


data = [1,2,3,4,5,6,7,8,9,10]

N = len(data)
jj = np.complex(0,1)

w = np.exp(-2*np.pi*jj / N)
W = w / math.sqrt(N)

w_mat = [ [  np.power(w, j*k)  for j in range(N) ] for k in range(N) ]


answer = multi(w_mat, data)

real = [np.real(a) for a in answer]
img = [np.imag(a) for a in answer]


plt.plot(real, label="real")
plt.plot(img, label="imaginary")
plt.grid()
plt.legend()
plt.show()