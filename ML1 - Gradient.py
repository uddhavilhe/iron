import numpy as np
def g(s,gf,mi,lr,b = 0.001):
    s1 = [s]
    x = s
    for i in range(mi):
        d = lr * gf(x)
        if(np.abs(d) < b):
            break
        x = x-d
        s1.append(x)
    return s1,x,lr

def gd_f(x):
    return 2 * x 

list,r,lr = g(2,gd_f,100,0.01)
print("The list elements are:")
print(list)
a = len(list)
print("The total elements are: ",a)
print("The optimal value :",r)
