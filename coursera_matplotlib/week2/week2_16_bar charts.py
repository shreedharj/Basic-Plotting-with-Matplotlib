import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

fig = plt.figure()
canvas = FigureCanvasAgg(fig)

linear_data = np.array([1,2,3,4,5,6,7,8])
quadratic_data = linear_data**2

xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width=0.3) #creates new bars for the linear data

new_xvals = []
for item in xvals:
    new_xvals.append(item+0.3) #shifts the red/quadratic bars to the right

plt.bar(new_xvals, quadratic_data, width=0.3, color='red') #creates new bars for the quadratic data

canvas.print_figure('images/week2_16_barcharts.png')

