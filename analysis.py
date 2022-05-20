import numpy as np
import scipy as sp
from matplotlib import pyplot as plt

# output of 2D simulation
pi_2d = [3.1919999999999997, 3.156, 3.1486400000000008, 3.1422, 3.1430840000000004, 3.141611599999999, 3.141634272]
# output of 3D simulation
pi_3d = [3.0120000000000005, 3.160800000000001, 3.1368000000000005, 3.1417919999999997, 3.1406604, 3.1407106799999998, 3.1418666040000005]
# true value of pi
pi = [3.14159265358979323846264338327950288419716939937510]*7
sample = [i for i in range(1,8,1)]

# plotting the points
plt.plot(sample,pi_2d)
plt.plot(sample,pi_3d)
plt.plot(sample,pi)
plt.gca().legend(('2D','3D','True Value'))
# naming the x axis
plt.xlabel('log10(sample_size)')
# naming the y axis
plt.ylabel('pi value')
# giving a title to my graph
plt.title('Monte Carlo simulation!')
# function to show the plot
plt.show()

# plotting the points
plt.plot(sample,[abs(x-y) for x,y in zip(pi,pi_2d)])
plt.plot(sample,[abs(x-y) for x,y in zip(pi,pi_3d)])
plt.plot(sample,[0 for x in range(7)])
plt.gca().legend(('2D','3D','Zero'))
# naming the x axis
plt.xlabel('log10(sample_size)')
# naming the y axis
plt.ylabel('pi value')
# giving a title to my graph
plt.title('Monte Carlo simulation!')
# function to show the plot
plt.show()

################################## ANALYSIS ##############################################################
#
# From above plots we can see that the 2D simulation approaches pi faster than the 3D.
#
# pi_2d = [3.1919999999999997, 3.156, 3.1486400000000008, 3.1422, 3.1430840000000004, 3.141611599999999, 3.141634272]
# pi_3d = [3.0120000000000005, 3.160800000000001, 3.1368000000000005, 3.1417919999999997, 3.1406604, 3.1407106799999998, 3.1418666040000005]
# pi = 3.14159265358979323846264338327950288419716939937510
#
# The first plot compares the obtained pi values to that of the true value of pi
# The second plot shows the absolute difference between the obtained and true showing that the 2D simulation approaches true pi faster.
#
################################## ANALYSIS ##############################################################
