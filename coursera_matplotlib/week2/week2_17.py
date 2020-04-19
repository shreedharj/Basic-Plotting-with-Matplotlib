import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

fig = plt.figure()
canvas = FigureCanvasAgg(fig)

linear_data = np.array([1,2,3,4,5,6,7,8])
quadratic_data = linear_data**2

xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width=0.3)

new_xvals = []
for item in xvals:
    new_xvals.append(item+0.3)

plt.bar(new_xvals, quadratic_data, width=0.3, color='red')

#calculating errors

from random import randint
linear_err = [randint(0,15) for x in range(len(linear_data))]
plt.bar(xvals, linear_data, width=0.3, yerr=linear_err)

canvas.print_figure('images/week2_17_barcharts.png')

