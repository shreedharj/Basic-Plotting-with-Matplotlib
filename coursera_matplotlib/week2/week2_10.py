import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

zip_generator = zip([1,2,3,4,5],[6,7,8,9,10])
x,y = zip(*zip_generator)
print(x)
print(y)

fig = plt.figure()
canvas = FigureCanvasAgg(fig)

plt.scatter(x[:2],y[:2], s=100, c='red', label='Tall students') #ledgend
plt.scatter(x[2:],y[2:], s=100, c='blue', label='Short students')

plt.xlabel('The number of times the child kicked the ball') #x-axis label
plt.ylabel('The grade of the student') #y-axis label
plt.title('Relationship between ball kicking and grades') #title

plt.legend()
plt.legend(loc=4, frameon=True, title='Ledgend') #loc means the position of the ledgend, frameon means the frame is visible

canvas.print_figure('images/week2_10.png')
