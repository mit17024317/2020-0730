from createGraph import plot
import numpy as np

def Rosenbrock(x):
    sum = 0
    for i in range(len(x)-1):
        sum += 100*(10*x[i+1] - 5 - (10*x[i]-5)**2)**2 + (1-10*x[i]-5)**2
    return sum/4000

def Rastrigin(x):
    n = len(x)
    sum = 10*n
    for t in x:
        t = 5.12*2*t-5.12
        sum += t**2-10*np.cos(2*np.pi*t)
    return sum/100

def Schwefel(x):
    sum = 0
    for t in x:
        t = 1000*t-500
        sum -= t*np.sin(np.sqrt(np.abs(t)))
    return sum/1000

if __name__ == "__main__":
    plot(Rosenbrock, 1)
    plot(Rosenbrock, 2, True)
    plot(Rastrigin, 1)
    plot(Rastrigin, 2, True)
    plot(Schwefel, 1)
    plot(Schwefel, 2, True)
    
