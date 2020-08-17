#!/usr/bin/env python3

from random import *
import matplotlib.pyplot as plt

RANGE_MIN = 0
RANGE_MAX = 1

labels = [
    'Health Insurance', 
    'Dining out', 
    'Utilities', 
    'Transportation',
    'Cell phone',
    'House cleaner',
    'Internet',
    'Rent',
    'Donations',
    'Groceries'
    ]
n_sections = len(labels) 
n_sizes = []

for s in range(n_sections):
    
    prop = uniform(RANGE_MIN, RANGE_MAX)
    n_sizes.append(prop)
    RANGE_MAX = RANGE_MAX - prop

print(n_sizes)

fig1, ax1 = plt.subplots()
ax1.pie(n_sizes, labels=labels)
ax1.axis('equal')
plt.show()
