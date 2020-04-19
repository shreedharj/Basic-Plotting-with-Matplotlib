import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

fig = plt.figure()
canvas = FigureCanvasAgg(fig)

linear_data = np.array([1,2,3,4,5,6,7,8])
quadratic_data = linear_data**2

xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width=0.3)

#stacked bar graphs
plt.bar(xvals, quadratic_data, width=0.3, bottom=linear_data, color='red') #bottom= makes the bars stcked

canvas.print_figure('images/week2_18_barcharts.png')

