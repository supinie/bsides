import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path


def plotLattice(ax, basis_vectors, ldown, rup, color, linewidth, alpha):
    """
    Draws a two-dimensional lattice.

    Args:
        ax: The Matplotlib Axes instance to plot on.
        basis_vectors: A list of two NumPy arrays representing the basis vectors of the lattice.
        ldown: A NumPy array representing the lower left corner of the rectangular area to draw the lattice in.
        rup: A NumPy array representing the upper right corner of the rectangular area to draw the lattice in.
        color: A string representing the color of the lattice points and basis vectors.
        linewidth: A float representing the linewidth of the lattice points.
        alpha: A float representing the alpha value of the lattice points.

    Returns:
        A list of NumPy arrays representing the lattice points.
    """
    
    # get the basis vectors
    b1, b2 = np.array(basis_vectors[0]), np.array(basis_vectors[1])
    # list to hold the lattice points
    points = []
    
    # upper bounds for the for loops
    xmax, ymax = 0, 0
    if b1[0] == 0:
        xmax = np.floor(rup[0] / abs(b2[0]))
    elif b2[0] == 0:
        xmax = np.floor(rup[0] / abs(b1[0]))
    else:
        xmax = np.floor(rup[0] / min(abs(b1[0]),abs(b2[0])))
    
    if b1[1] == 0:
        ymax = np.floor(rup[1] / abs(b2[1]))
    elif b2[1] == 0:
        ymax = np.floor(rup[1] / abs(b1[1]))
    else:
        ymax = np.floor(rup[1] / min(abs(b1[1]),abs(b2[1])))
    
    # increase the bounds by 1
    xmax = int(xmax) + 50
    ymax = int(ymax) + 50
    
    # get the lower bounds for the for loops
    xmin, ymin = -int(xmax), -int(ymax)
    
    for i in range(xmin, int(xmax)):
        for j in range(ymin, int(ymax)):
            # make the linear combination
            p = i * b1 + j * b2
            # if the point is within the plotting area, plot it and add the point to the list
            if ldown[0] <= p[0] <= rup[0] and ldown[1] <= p[1] <= rup[1]:
                ax.scatter(p[0], p[1], color='gray', linewidths=5, alpha=1)
                points.append(p)

    # plot basis vectors
    # ax.quiver(0, 0, b1[0], b1[1], color='red', scale_units='xy', scale=1, alpha=1)
    # ax.quiver(0, 0, b2[0], b2[1], color='blue', scale_units='xy', scale=1, alpha=1)
    # ax.quiver(0, 0, b2[0] + b1[0], b2[1] + b1[1], color='red', scale_units='xy', scale=1, alpha=1)
    # ax.quiver(0, 0, 2 * b2[0] + b1[0], 2 * b2[1] + b1[1], color='blue', scale_units='xy', scale=1, alpha=1)


    return points


def plotParallelepipeds(ax, bad_basis_vectors, points, color, linewidth, alpha):
    b1, b2 = np.array(bad_basis_vectors[0]), np.array(bad_basis_vectors[1])
    ax.quiver(0, 0, b1[0], b1[1], color='red', scale_units='xy', scale=1, alpha=1)
    ax.quiver(0, 0, b2[0], b2[1], color='blue', scale_units='xy', scale=1, alpha=1)

    # Example new vectors (replace with your actual new vectors)
    new_vec1 = np.array([3, -1])
    new_vec2 = np.array([2, 3])

    # Find lengths of the original vectors
    length_b1 = np.linalg.norm(b1)
    length_b2 = np.linalg.norm(b2)

    # Normalize the new vectors (scale them to unit length)
    new_vec1_normalized = new_vec1 / np.linalg.norm(new_vec1)
    new_vec2_normalized = new_vec2 / np.linalg.norm(new_vec2)

    # Scale the new vectors to have the same length as b1 and b2
    new_vec1_scaled = new_vec1_normalized * length_b1
    new_vec2_scaled = new_vec2_normalized * length_b2
    ax.quiver(0, 0, new_vec1_scaled[0], new_vec1_scaled[1], color='red', scale_units='xy', scale=1, alpha=0.25)
    ax.quiver(0, 0, new_vec2_scaled[0], new_vec2_scaled[1], color='blue', scale_units='xy', scale=1, alpha=0.25)
    ax.quiver(0, 0, new_vec1[0], new_vec1[1], color='red', scale_units='xy', scale=1, alpha=0.25)
    ax.quiver(0, 0, new_vec2[0], new_vec2[1], color='blue', scale_units='xy', scale=1, alpha=0.25)
    # e = [-0.506185, -0.99403]
    # ax.scatter(6 - e[0], 7 - e[1], color='green', linewidths=5, alpha=1)
    # ax.scatter(6, 7, color='red', linewidths=5, alpha=1)
    # for p in points:
    #     # Calculate the center offset
    #     center_offset = (b1 + b2) / 2
    #     # Define vertices for the parallelepiped centered on the lattice point
    #     vertices = [p - center_offset, p - center_offset + b1, p - center_offset + b1 + b2, p - center_offset + b2]
    #     path = Path(vertices)
    #     if path.contains_point(np.array([6 - e[0], 7 - e[1]])):
    #         fill_color = 'yellow'
    #         fill_alpha = 0.3
    #     else:
    #         fill_color = 'none'
    #         fill_alpha = 0.3
    #     parallelepiped = patches.Polygon(vertices, closed=True, fill=True, edgecolor=color, linewidth=linewidth, alpha=fill_alpha, facecolor=fill_color)
    #     ax.add_patch(parallelepiped)


if __name__ == '__main__':
    
    # Define original basis
    b1 = np.array([-3.18068, -2.83395])
    b2 = np.array([2.6236, -4.57916])
    basis_vectors = [b1, b2]

    # Define a "bad" basis
    bad_b1 = np.array([5, 4])
    bad_b2 = np.array([9, 5])
    bad_basis_vectors = [bad_b1, bad_b2]

    # define the plotting area
    ldown = np.array([-12.8, -12.8])
    rup = np.array([12.8, 12.8])

    fig, ax = plt.subplots()
    points = plotLattice(ax, basis_vectors, ldown, rup, 'blue', 3, 0.25)
    plotParallelepipeds(ax, basis_vectors, points, 'green', 1, 0.25)

    # resize the plotting window
    mngr = plt.get_current_fig_manager()
    mngr.resize(960, 1080)
    
    # tune axis
    ax.set_aspect('equal')
    ax.grid(True, which='both')
    ax.set_xlim(ldown[0], rup[0])
    ax.set_ylim(ldown[1], rup[1])

# Hide axis but keep the grid
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)    
    # show the plot
    plt.show()
