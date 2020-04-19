import matplotlib.pyplot as plt

from matplotlib.backends.backend_agg import FigureCanvasAgg  #*
from matplotlib.figure import Figure   #*

fig = Figure()
canvas = FigureCanvasAgg(fig)

ax = fig.add_subplot(2,2,2) #first two numbers are the grid coordinate (for ex. 2x2,3x3,5x2). Third number is the location
ax.plot(3,2,'.')
ax.axis([0,6,0,10]) #dimentions of the x and y axes

ax1 = fig.add_subplot(2,2,3)
ax1.plot(2,6,'.')
ax1.axis([0,6,0,12])

canvas.print_png('images/week2_2.png')

