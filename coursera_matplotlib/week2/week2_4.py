import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure


fig = plt.figure()
canvas = FigureCanvasAgg(fig)

plt.plot (5,3,'o') #first two numbers is the coordinate. Third is the symbol of that coordinate
plt.plot (6,5,'v')
plt.plot (2,1,'x')


ax = plt.gca()
ax.axis([0,10,0,12])

canvas.print_figure('images/week2_4.png')



#gcf means get current figure
#gca means get current axes