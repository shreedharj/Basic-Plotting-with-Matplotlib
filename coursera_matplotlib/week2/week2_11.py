import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

linear_data = np.array([1,2,3,4,5,6,7,8])
quadratic_data = linear_data**2 #linear data to the power of 2

fig = plt.figure()
canvas = FigureCanvasAgg(fig)

plt.plot(linear_data, '-o', quadratic_data, '-o') #'-o' connects the dots

canvas.print_figure('images/week2_11.png')
