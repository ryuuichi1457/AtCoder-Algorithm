def f(x):
    if x==0:
        return 1
    return x**f(x-1)
import math
def g(x):   
    if x==0:
        return 0
    return (math.log10(x))*g(x-1)
print(g(1))