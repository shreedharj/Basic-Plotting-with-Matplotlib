import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

x = np.array([1,2,3,4,5,6,7,8])
y = x
colors = ['green']*(len(x)-1) #all points but the last one are green (length-1)
colors.append('red') #append means to add

fig = plt.figure()
canvas = FigureCanvasAgg(fig)

plt.scatter(x,y, s=100,c=colors) #s means size. c meaning colors was already declared in lines 7-8
  
canvas.print_figure('images/week2_7.png')

