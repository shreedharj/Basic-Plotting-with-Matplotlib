import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure


fig = plt.figure()
canvas = FigureCanvasAgg(fig)

plt.plot (3,2,'o')
ax = plt.gca()
ax.axis([0,4,0,3])

canvas.print_figure('images/week2_3.png')

#gcf means get current figure
#gca means get current axes