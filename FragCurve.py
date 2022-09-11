from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
from scipy import optimize
from math import factorial


t_12, b_12 = [0.44791569, 0.31070075]
t_13, b_13 = [1.50545199, 0.32777167]
t_23, b_23 = [1.4,0.4]

#1-->2
x = np.arange(0, 1.2, 0.01)
y = stats.norm.cdf(np.log(x/t_12)/b_12,0,1)
plt.plot([1,1],[0, stats.norm.cdf(np.log(1/t_12)/b_12,0,1)])
plt.plot(x,y)
plt.xlabel('Peak Ground Acceleration (g)')
plt.ylabel('Cumulative Probability')
plt.title('Transitioning from H1 to H2')
plt.grid(visible = True, linewidth = 0.5)
plt.show()

#1-->3
x = np.arange(0, 3.5, 0.01)
y = stats.norm.cdf(np.log(x/t_13)/b_13,0,1)
plt.plot([1,1],[0, stats.norm.cdf(np.log(1/t_13)/b_13,0,1)])
plt.plot(x,y)
plt.xlabel('Peak Ground Acceleration (g)')
plt.ylabel('Cumulative Probability')
plt.title('Transitioning from H1 to H3')
plt.grid(visible = True, linewidth = 0.5)
plt.show()

#2-->3
x = np.arange(0, 3.5, 0.01)
y = stats.norm.cdf(np.log(x/t_23)/b_23,0,1)
plt.plot([1,1],[0, stats.norm.cdf(np.log(1/t_23)/b_23,0,1)])
plt.plot(x,y)
plt.xlabel('Peak Ground Acceleration (g)')
plt.ylabel('Cumulative Probability')
plt.title('Transitioning from H2 to H3')
plt.grid(visible = True, linewidth = 0.5)
plt.show()


#Code used to solve for the paramethers theta (t) and beta (b)
'''
m = 13
r =     [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]
n =     [2, 1, 5, 4, 6, 7, 5, 8, 3, 4, 1, 3, 1]
f_2 = [0, 0, 0, 1, 5, 6, 3, 8, 2, 4, 1, 2, 1]
f_2 =   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]

def E( params ):
    t, b = params
    sum = 0
    for i in range(m):
        p_i = stats.norm.cdf(np.log(r[i]/t)/b,0,1)
        P_i = n[i]*(p_i-(f_2[i]/n[i]))**2
        sum += P_i
    return sum

def L( params ):
    t, b = params
    mult = 1
    for i in range(m):
        p_i = stats.norm.cdf(np.log(r[i]/t)/b,0,1)
        P_i = p_i**f_2[i] * (1-p_i)**(n[i]-f_2[i]) * factorial(n[i]) / (factorial(f_2[i])*factorial(n[i]-f_2[i]))
        mult *= P_i
    return (1/mult)


print(optimize.minimize(L,[0.3,1]))


while True:
    acc = float(input('Peak Ground Acceleration (g): '))
    prob = stats.norm.cdf(np.log(acc/1.68)/0.4,0,1)
    print('Cumulative Probability of Failure: '+ str(prob))
    if input('Exit? (Y/N) ') == 'Y':
        break
'''

