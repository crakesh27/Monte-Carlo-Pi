import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# class point to contain the geometric point both 2d/3d and required functions
class Point:
    """
    point class
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.dim = 2
        if(z is not None):
            self.z = z
            self.dim = 3

    def distance(self, x, y, z):
        """
        returns cartesian distance between the two points
        """
        if z is not None:
            return np.sqrt((self.x-x)**2 + (self.y-y)**2 + (self.z-z)**2)
        return np.sqrt((self.x-x)**2 + (self.y-y)**2)

    def display(self):
        """
        prints the point
        """
        print("x =", self.x)
        print("y =", self.y)
        if(self.dim == 3):
            print("z =", self.z)

    def getX(self):
        """
        getter function for x coordinate
        """
        return self.x

    def getY(self):
        """
        getter function for y coordinate
        """
        return self.y

    def getZ(self):
        """
        getter function for z coordinate
        """
        if self.dim == 2:
            return None
        return self.z


def init():
    global sample_size
    global sample_factor
    global runs
    global radius
    # defining variables
    sample_size = 1
    sample_factor = 10
    runs = 7
    radius = 1


def MonteCarlo2D(bool):

    def generate_points():
        """
        generating the required number of points(sample_size) and returning it
        """
        points = []
        for i in range(sample_size):
            x, y = np.random.uniform(-1*radius, 1 *
                                     radius), np.random.uniform(-1*radius, 1*radius)
            points.append(Point(x, y, None))
        points = np.array(points)
        return points

    def plot(x_circle, y_circle, x_square, y_square):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.scatter(x_circle, y_circle, color='g', marker='s', s=1)
        ax.scatter(x_square, y_square, color='r', marker='s', s=1)
        fig.show()
        plt.show()

    def simulation(display_plot):
        """
        Monte Carlo simulation driver function
        """
        global sample_size
        output = []
        for i in range(runs):
            sample_size *= sample_factor
            points = generate_points()
            circle = 0
            square = 0
            x_circle, y_circle, x_square, y_square = [], [], [], []
            for point in points:
                if point.distance(0, 0, None) <= radius:
                    circle += 1
                    x_circle.append(point.getX())
                    y_circle.append(point.getY())
                else:
                    x_square.append(point.getX())
                    y_square.append(point.getY())
                square += 1
            print("[Run "+str(i+1)+",Sample "+str(sample_size) +
                  "] Estimate of pi =", 4*circle/square)
            output.append(4*circle/square)
            if display_plot:
                plot(x_circle, y_circle, x_square, y_square)
        return output

    return simulation(bool)


def MonteCarlo3D(bool):

    def plot(x_sphere, y_sphere, z_sphere, x_cube, y_cube, z_cube):
        # 3d view
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_aspect('equal')
        ax.scatter(x_sphere, y_sphere, z_sphere, color='g', marker='s')
        ax.scatter(x_cube, y_cube, z_cube, color='r', marker='s')
        fig.show()
        plt.show()
        # 3d view
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_aspect('equal')
        ax.scatter(x_sphere, y_sphere, z_sphere, color='g', marker='s')
        fig.show()
        plt.show()
        # 2d view
        # fig = plt.figure()
        # plt.subplot(1, 3, 1)
        # plt.scatter(x_sphere, y_sphere, color='g', marker='s')
        # plt.scatter(x_cube, y_cube, color='r', marker='s')
        # plt.subplot(1, 3, 2)
        # plt.scatter(y_sphere, z_sphere, color='g', marker='s')
        # plt.scatter(y_cube, z_cube, color='r', marker='s')
        # plt.subplot(1, 3, 3)
        # plt.scatter(x_sphere, z_sphere, color='g', marker='s')
        # plt.scatter(x_cube, z_cube, color='r', marker='s')
        # plt.show()

    def generate_points():
        """
        generating the required number of points(sample_size) and returning it
        """
        points = []
        for i in range(sample_size):
            x, y, z = np.random.uniform(-1*radius, 1*radius), np.random.uniform(-1 *
                                                                                radius, 1*radius), np.random.uniform(-1*radius, 1*radius)
            points.append(Point(x, y, z))
        points = np.array(points)
        return points

    def simulation(display_plot):
        """
        Monte Carlo simulation driver function
        """
        global sample_size
        output = []
        for i in range(runs):
            sample_size *= sample_factor
            points = generate_points()
            sphere = 0
            cube = 0
            x_sphere, y_sphere, z_sphere, x_cube, y_cube, z_cube = [], [], [], [], [], []
            for point in points:
                if point.distance(0, 0, 0) <= radius:
                    sphere += 1
                    x_sphere.append(point.getX())
                    y_sphere.append(point.getY())
                    z_sphere.append(point.getZ())
                else:
                    x_cube.append(point.getX())
                    y_cube.append(point.getY())
                    z_cube.append(point.getZ())
                cube += 1
            print("[Run "+str(i+1)+",Sample "+str(sample_size) +
                  "] Estimate of pi =", 6*sphere/cube)
            output.append(6*sphere/cube)
            if display_plot:
                plot(x_sphere, y_sphere, z_sphere, x_cube, y_cube, z_cube)
        return output

    return simulation(bool)


if __name__ == "__main__":
    # Monte Carlo 2D simulation
    print("Monte Carlo 2D simulation")
    init()
    # set true if you want to plot
    result2 = MonteCarlo2D(True)
    # Monte Carlo 3D simulation
    print("Monte Carlo 3D simulation")
    init()
    # set true if you want to plot
    result3 = MonteCarlo3D(False)
