import matplotlib.pyplot as plt
import numpy as np
import random

import duplicate

import insertion
import selection
import bogo

def permute(n):
    ordered = [i for i in range(1, n+1)]
    permutation = []
    for i in range(0,len(ordered)):
        choice = random.choice(ordered)
        ordered.remove(choice)
        permutation.append(choice)
    return permutation

n = 50

starting = permute(n)

insertionlist = duplicate.dup(starting)
selectionlist = duplicate.dup(starting)
# bogolist = duplicate.dup(starting)

insertionStates = insertion.insertion(insertionlist)
selectionStates = selection.selection(selectionlist)
# bogoStates = bogo.bogo(bogolist)

insertionN = len(insertionStates)
selectionN = len(selectionStates)
# bogoN = len(bogoStates)

from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers

fig = plt.figure()
ax = plt.axes(xlim=(0, n), ylim=(0,n))

lines = []

for i in range(0,2):
    lobj = ax.plot([], [], lw=3)[0]
    lines.append(lobj)

def init():
    for line in lines:
        line.set_data([], [])
    return lines

def animate(i):
    if i < insertionN:
        insertionx = [i for i in range(0,n)]
        insertiony = insertionStates[i]
    else:
        insertionx = [i for i in range(0,n)]
        insertiony = insertionStates[insertionN-1]
        
    if i < selectionN:
        selectionx = [i for i in range(0,n)]
        selectiony = selectionStates[i]
    else:
        selectionx = [i for i in range(0,n)]
        selectiony = selectionStates[selectionN-1]

    # if i < bogoN:
    #     bogox = [i for i in range(0,n)]
    #     bogoy = bogoStates[i]
    # else:
    #     bogox = [i for i in range(0,n)]
    #     bogoy = bogoStates[bogoN-1]

    xlist = [insertionx, selectionx]
    ylist = [insertiony, selectiony]
    
    for lnum,line in enumerate(lines):
        line.set_data(xlist[lnum], ylist[lnum]) # set data for each line separately. 

    return lines

frameNum = max(insertionN, selectionN)

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=frameNum+100, interval=2, blit=True)

plt.show()