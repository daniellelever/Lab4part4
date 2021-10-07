#PART 4: Group 10: done by Danielle Lever

import numpy as np
import scipy.integrate as scint
import matplotlib.pyplot as plt


#inital conditons =  y(t=0) = [maxswing, 0 ,0]
pen_length =  9.81 #m
amp_period = 2 * (np.pi)
maxswing = (np.pi)/6 # in rad

def pendulum_amp(time, theatastate, maxswing, Q_damp):
    theataprime = theatastate[1]
    theataprime2 = -1 / Q_damp * theataprime - np.sin(theatastate[0])
    return([theataprime, theataprime2])


def event(time, theatastate, maxswing, Q_damp):
    x = pendulum_amp(time, theatastate, maxswing, Q_damp)
    return theatastate[1]
    
pendulum_amp.terminal = True

Q_damp = [1,5,10,25,50]
t_soln = np.linspace(0,10*np.pi,10000)
yinit = np.array([0,maxswing])

   
for Q in Q_damp:
    result = scint.solve_ivp(pendulum_amp, [0,10*np.pi], yinit, \
                               args=(maxswing, 2), events=[event])

peakval = result.y_events
timeest = result.t_events
inital = peakval[0]/np.exp(1)