import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

fig = plt.figure()
canvas = FigureCanvasAgg(fig)

linear_data = np.array([1,2,3,4,5,6,7,8])
quadratic_data = linear_data**2

xvals = range(len(linear_data))
plt.barh(xvals, linear_data, height=0.3, color='g')

#horizontally stacked bar graphs
plt.barh(xvals, quadratic_data, height=0.3, left=linear_data, color='red') #changing width to height and bottom to left make the bars stacked sideways

canvas.print_figure('images/week2_19_barcharts.png')

