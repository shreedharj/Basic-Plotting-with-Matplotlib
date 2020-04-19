import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

zip_generator = zip([1,2,3,4,5],[6,7,8,9,10])
x,y = zip(*zip_generator)
print(x)
print(y)

fig = plt.figure()
canvas = FigureCanvasAgg(fig)

#:x means from the start of the list to number x and x: means x onwards till the end of the list
plt.scatter(x[:2],y[:2], s=100, c='red', label='Tall students')
plt.scatter(x[2:],y[2:], s=100, c='blue', label='Short students')

canvas.print_figure('images/week2_9.png') #(the plot looks wrong)
