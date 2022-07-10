# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation


# def data_gen(t=0):
#     cnt = 0
#     while cnt < 1000:
#         cnt += 1
#         t += 0.1
#         yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)


# def init():
#     ax.set_ylim(-1.1, 1.1)
#     ax.set_xlim(0, 10)
#     del xdata[:]
#     del ydata[:]
#     line.set_data(xdata, ydata)
#     return line,

# fig, ax = plt.subplots()
# line, = ax.plot([], [], lw=2)
# ax.grid()
# xdata, ydata = [], []


# def run(data):
#     # update the data
#     t, y = data
#     xdata.append(t)
#     ydata.append(y)
#     xmin, xmax = ax.get_xlim()

#     if t >= xmax:
#         ax.set_xlim(xmin, 2*xmax)
#         ax.figure.canvas.draw()
#     line.set_data(xdata, ydata)

#     return line,

# ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
#                               repeat=False, init_func=init)
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np

# grid = np.random.random((10,10))

# fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, figsize=(6,10))

# ax1.imshow(grid, extent=[0,100,0,1])
# ax1.set_title('Default')

# ax2.imshow(grid, extent=[0,100,0,1], aspect='auto')
# ax2.set_title('Auto-scaled Aspect')

# ax3.imshow(grid, extent=[0,100,0,1], aspect=100)
# ax3.set_title('Manually Set Aspect')

# plt.tight_layout()
# plt.show()
# import numpy as np 
# import matplotlib.pyplot as plt

# # Generate some data
# nrows, ncols = 1000, 1000
# xmin, xmax = -32.4, 42.0
# ymin, ymax = 78.9, 101.3

# dx = (xmax - xmin) / (ncols - 1)
# dy = (ymax - ymin) / (ncols - 1)

# x = np.linspace(xmin, xmax, ncols)
# y = np.linspace(ymin, ymax, nrows)
# x, y = np.meshgrid(x, y)
# print(x,y)
# z = np.hypot(x - x.mean(), y - y.mean())
# x, y, z = [item.flatten() for item in (x,y,z)]

# # Scramble the order of the points so that we can't just simply reshape z
# indicies = np.arange(x.size)
# np.random.shuffle(indicies)
# x, y, z = [item[indicies] for item in (x, y, z)]

# # Up until now we've just been generating data...
# # Now, x, y, and z probably represent something like you have.

# # We need to make a regular grid out of our shuffled x, y, z indicies.
# # To do this, we have to know the cellsize (dx & dy) that the grid is on and
# # the number of rows and columns in the grid. 

# # First we convert our x and y positions to indicies...
# idx = np.round((x - x.min()) / dx).astype(np.int)
# idy = np.round((y - y.min()) / dy).astype(np.int)

# # Then we make an empty 2D grid...
# grid = np.zeros((nrows, ncols), dtype=np.float)

# # Then we fill the grid with our values:
# grid[idy, idx] = z

# # And now we plot it:
# plt.imshow(grid, interpolation='nearest', 
#         extent=(x.min(), x.max(), y.max(), y.min()))
# plt.colorbar()
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# generate 101 x and y values between -10 and 10 
x = np.linspace(-10, 10, 101)
y = np.linspace(-10, 10, 101)

# make X and Y matrices representing x and y values of 2d plane
X, Y = np.meshgrid(x, y)

# compute z value of a point as a function of x and y (z = l2 distance form 0,0)
Z = np.sqrt(X ** 2 + Y ** 2)

# # plot filled contour map with 100 levels
cs = plt.contourf(X, Y, Z, 100)
print(cs)
# # add default colorbar for the map
# plt.colorbar(cs)