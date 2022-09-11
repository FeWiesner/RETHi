import random as rd
from scipy import stats
import numpy as np

#Theta and Beta values found following Potter, methods B and C
t_12, b_12 = [0.44791569, 0.31070075]
t_13, b_13 = [1.50545199, 0.32777167]
t_23, b_23 = [1.4,0.4]

#Functions from the fragility curves
def one_two(pga):
    return stats.norm.cdf(np.log(pga/t_12)/b_12,0,1)

def one_three(pga):
    return stats.norm.cdf(np.log(pga/t_13)/b_13,0,1)

def two_three(pga):
    return stats.norm.cdf(np.log(pga/t_23)/b_23,0,1)


def matrices(E): #transition matrices dependent on intensity of EQs
    M = []
    for i in E:
        m = []
        m.append([1-one_two(i), one_two(i) - one_three(i), one_three(i)])
        m.append([0, 1-two_three(i), two_three(i)])
        m.append([0, 0, 1])
        M.append(m)
    return M 

def quakes(maximum, step): #function to determine how fine the step between PGAs will be (ex: 0.1, 0.2... or 0.001, 0.002...)
    E = []
    e = 0
    while e < maximum:
        e += step
        E.append(round(e,1))
    return E #returns a list of EQ intensities, feed to matrices func

'''
RESEARCH: Is there a function that models the frequency of EQs given their intensity? I only looked up in USGS database for all EQs in some region in the last 120 yrs
and divided amount by time

If such function exists, define it to find the frequencies, using the same step used for the intensities
'''

def freqs(step, maximum):
    #TO-DO
    pass



def run():

    #T = float(input('Total time (yrs): '))
    T = 100 #years

    Q = 1 #starts at HS1

    # EQ = quakes(float(input('Largest PGA(g, NOT m/s2): ')), float(input('Step size between quake intensities (g, NOT m/s2): ')),) list of EQs
    EQ = quakes(1.3, 0.1)
    

    M = matrices(EQ) #List of all transition matrices

    betas = [141, 
            2.40, 
            1.75, 
            0.892, 
            0.637, 
            0.284, 
            0.333, 
            0.118, 
            0.039, 
            0.030, 
            0.029, 
            0.012, 
            0.0098] #frequency of changes, here I input manually but ideally use the freqs function

    t = 0

    event_times = []
    moments = []

    events = {}
    for i in EQ:
        events[i] = 0


    for i in betas: #one occurrence of all poisson, saves the time at which they will occur
        event_times.append(rd.expovariate(i))

    while t < T:
        minimo = min(event_times) #finds first occurrence
        t = minimo #moves to time of next event
        occurred = event_times.index(minimo) #finds the index of the EQ that occurred

        events[EQ[occurred]] += 1 #keeps track of all the events of some intensity


       
        Q = rd.choices([1,2,3], M[occurred][Q-1])[0] #according to the matrix, sees whther it transitions or not


        if  Q == 2 and moments == []: #records first transition to H2
            moments.append(t)
        
        if Q ==3 and len(moments) == 1: #records frist transition to H3
            moments.append(t)
            final = EQ[occurred]
            break

        event_times[occurred] += rd.expovariate(betas[occurred])
    if len(moments) == 0:
        moments = [-1,-1]
        final = -1
    elif len(moments) == 1:
        moments.append(-1)
        final = -1
    return(moments, events, final)

with open('Model Runs.csv', 'w') as w:
    header = 't_h2, t_h3, '
    for i in range(1,14):
        header += 'q_' + str(i/10) + ', '
    header += 'final_int'
    w.write(header+'\n')
    for i in range(10000):
        result = run()
        line = str(round(result[0][0],3)) + ', '
        line += str(round(result[0][1],3)) + ', '
        for value in result[1].values():
            line += str(value) + ', '
        line += str(result[2])
        w.write(line+'\n')

