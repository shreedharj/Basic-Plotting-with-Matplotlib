import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

linear_data = np.array([1,2,3,4,5,6,7,8])
quadratic_data = linear_data**2

fig = plt.figure()
canvas = FigureCanvasAgg(fig)

plt.plot(linear_data, '-o', quadratic_data, '-o')
plt.plot([22,44,55], '--r') #'--r' connects the dots with a dotted line
plt.xlabel('Some data')
plt.ylabel('Some other data')
plt.title('A title')
plt.legend(['Baseline','Competition','Us'])

plt.gca().fill_between(range(len(linear_data)),linear_data,quadratic_data,facecolor='blue',alpha=0.25)
    #fills the area between two graphs with a color. Alpha value changes the color depth

canvas.print_figure('images/week2_12.png')
