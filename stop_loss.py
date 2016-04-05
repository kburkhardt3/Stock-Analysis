"""
This program simulates the effect of using a trailing stop loss at a set
percentage below market value to sell a stock which undergoes a random walk.

Stock is purchased at $100 and undergoes daily fluctuations chosen from
a normal distribution defined by mu and sigma. The simulation records the
selling prices and how many days the stock took to sell.
"""

import random
#import matplotlib.pyplot as plt
import numpy as np

def stop_loss(percent, volatility):
    
    mu = 0
    sigma = volatility
    fraction = percent/100 # adjusts percent to multiplier
    
    p_hist = [] # initiates a price history
    day_hist = [] # initiates a day history
    
#    for k in range(5): # volatility from 1% to 5%
#    
#        for j in range (5): # percent from 1% to 5%
    
    for i in range(1000): # runs simulation 1,000 times
    
        price = 100 # buying price of $100        
        stop_loss = price - price*fraction # sets stop at percent lower than price
        day = 0
        sell = 0
        while sell == 0:
            fluctuation = random.gauss(mu,sigma) # generates random number from norm(0,1)
            price += fluctuation
            
            if price < stop_loss: # triggers sell and records price if price < stop_loss
                p_hist.append(stop_loss)
                day_hist.append(day)
                sell = 1
                
            if fluctuation > 0: # updates stop_loss if price rises
                stop_loss = price - price*fraction
            
            day += 1 # passing of another day
                
    print(np.mean(p_hist))
    print(np.mean(day_hist))
