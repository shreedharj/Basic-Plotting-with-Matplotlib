import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

x = np.array([1,2,3,4,5,6,7,8]) #multiple coordinates
y = x #y points are same as x (linear line)

fig = plt.figure()
canvas = FigureCanvasAgg(fig)

plt.scatter(x,y) #scatter plot

canvas.print_figure('images/week2_6.png')

