import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure


fig = plt.figure()
canvas = FigureCanvasAgg(fig)

plt.plot (5,3,'o')
plt.plot (6,5,'v')
plt.plot (2,1,'x')


ax = plt.gca() #(dont understand the output)
ax.axis([0,10,0,12])

canvas.print_figure('images/week2_5.png')

ax = plt.gca()
children = ax.get_children()
for child in children:
        print(child)

#A spine is a axis