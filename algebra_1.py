"""
Calculate Magnitude: To calculate the magnitude of a 2D2D2D vector we will use the Pythagorean Theorem.
Calculate Direction: θ=tan−1(y/x)​
"""

"""Plotting a Vector in 2D"""

# Import NumPy and Matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Define vector v
v = np.array([1, 1])

# Plots vector v as blue arrow with red dot at origin (0,0) using Matplotlib
# Creates axes of plot referenced 'ax'
ax = plt.axes()

# Plots red dot at origin (0,0)
ax.plot(0, 0, 'or')

# Plots vector v as blue arrow starting at origin 0,0
ax.arrow(0, 0, *v, color='b', linewidth=2.0, head_width=0.20, head_length=0.25)

# Sets limit for plot for x-axis
plt.xlim(-2, 2)

# Set major ticks for x-axis
major_xticks = np.arange(-2, 3)
ax.set_xticks(major_xticks)

# Sets limit for plot for y-axis
plt.ylim(-1, 2)

# Set major ticks for y-axis
major_yticks = np.arange(-1, 3)
ax.set_yticks(major_yticks)

# Creates gridlines for only major tick marks
plt.grid(b=True, which='major')

# Displays final plot
plt.show()

"""
Scaling a Vector using a Scalar
"""

# Define vector v
v = np.array([1, 1])

# Define scalar a
a = 3

# TODO 1.: Define vector av - as vector v multiplied by scalar a
av = np.array(v * a)

# Plots vector v as blue arrow with red dot at origin (0,0) using Matplotlib
# Creates axes of plot referenced 'ax'
ax = plt.axes()

# Plots red dot at origin (0,0)
ax.plot(0, 0, 'or')

# Plots vector v as blue arrow starting at origin 0,0
ax.arrow(0, 0, *v, color='b', linewidth=2.5, head_width=0.30, head_length=0.35)

# TODO 2.: Plot vector av as dotted (linestyle='dotted') vector of cyan color (color='c')
# using ax.arrow() statement above as template for the plot
ax.arrow(0, 0, *av, color='c', linewidth=2.5, head_width=0.30, head_length=0.35, linestyle='dotted')

# Sets limit for plot for x-axis
plt.xlim(-2, 4)

# Set major ticks for x-axis
major_xticks = np.arange(-2, 4)
ax.set_xticks(major_xticks)

# Sets limit for plot for y-axis
plt.ylim(-1, 4)

# Set major ticks for y-axis
major_yticks = np.arange(-1, 4)
ax.set_yticks(major_yticks)

# Creates gridlines for only major tick marks
plt.grid(b=True, which='major')

# Displays final plot
plt.show()

"""
Adding Two Vectors Together
"""

# Define vector v
v = np.array([1, 1])

# Define vector w
w = np.array([-2, 2])

# Plots vector v(blue arrow) and vector w(cyan arrow) with red dot at origin (0,0)
# using Matplotlib

# Creates axes of plot referenced 'ax'
ax = plt.axes()

# Plots red dot at origin (0,0)
ax.plot(0, 0, 'or')

# Plots vector v as blue arrow starting at origin 0,0
ax.arrow(0, 0, *v, color='b', linewidth=2.5, head_width=0.30, head_length=0.35)

# Plots vector w as cyan arrow starting at origin 0,0
ax.arrow(0, 0, *w, color='c', linewidth=2.5, head_width=0.30, head_length=0.35)

# Sets limit for plot for x-axis
plt.xlim(-3, 2)

# Set major ticks for x-axis
major_xticks = np.arange(-3, 2)
ax.set_xticks(major_xticks)

"""
Plotting Vector Addition
"""
# Define vector v
v = np.array([1,1])

# Define vector w
w = np.array([-2,2])

# DONE 1.: Define vector vw by adding vectors v and w
vw = v + w

# Plot that graphically shows vector vw (color='b') - which is the result of
# adding vector w(dotted cyan arrow) to vector v(blue arrow) using Matplotlib

# Creates axes of plot referenced 'ax'
ax = plt.axes()

# Plots red dot at origin (0,0)
ax.plot(0,0,'or')

# Plots vector v as blue arrow starting at origin 0,0
ax.arrow(0, 0, *v, color='b', linewidth=2.5, head_width=0.30, head_length=0.35)

# Plots vector w as cyan arrow with origin defined by vector v
ax.arrow(v[0], v[1], *w, linestyle='dotted', color='c', linewidth=2.5,
         head_width=0.30, head_length=0.35)

# DONE 2.: Plot vector vw as black arrow (color='k') with 3.5 linewidth (linewidth=3.5)
# starting vector v's origin (0,0)
ax.arrow(0, 0, *vw, color='k', linewidth=3.5, head_width=0.30, head_length=0.35)


# Sets limit for plot for x-axis
plt.xlim(-3, 2)

# Set major ticks for x-axis
major_xticks = np.arange(-3, 2)
ax.set_xticks(major_xticks)


# Sets limit for plot for y-axis
plt.ylim(-1, 4)

# Set major ticks for y-axis
major_yticks = np.arange(-1, 4)
ax.set_yticks(major_yticks)

# Creates gridlines for only major tick marks
plt.grid(b=True, which='major')

# Displays final plot
plt.show()