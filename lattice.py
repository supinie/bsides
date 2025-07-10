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
    search_radius = 30  # number of steps in each direction of i and j

    xmin, xmax = -search_radius, search_radius
    ymin, ymax = -search_radius, search_radius
    
    for i in range(xmin, int(xmax)):
        for j in range(ymin, int(ymax)):
            # make the linear combination
            p = i * b1 + j * b2
            # if the point is within the plotting area, plot it and add the point to the list
            if ldown[0] <= p[0] <= rup[0] and ldown[1] <= p[1] <= rup[1]:
                ax.scatter(p[0], p[1], color='gray', linewidths=5, alpha=alpha)
                points.append(p)

    # plot basis vectors
    ax.quiver(0, 0, b1[0], b1[1], color='red', scale_units='xy', scale=1, alpha=0.25)
    ax.quiver(0, 0, b2[0], b2[1], color='blue', scale_units='xy', scale=1, alpha=0.25)
    # ax.quiver(0, 0, b2[0] + b1[0], b2[1] + b1[1], color='red', scale_units='xy', scale=1, alpha=1)
    # ax.quiver(0, 0, 2 * b2[0] + b1[0], 2 * b2[1] + b1[1], color='blue', scale_units='xy', scale=1, alpha=1)


    return points


def plotParallelepipeds(ax, bad_basis_vectors, points, color, linewidth, alpha, target, e):
    b1, b2 = np.array(bad_basis_vectors[0]), np.array(bad_basis_vectors[1])
    # ax.quiver(0, 0, b1[0], b1[1], color='red', scale_units='xy', scale=1, alpha=1)
    # ax.quiver(0, 0, b2[0], b2[1], color='blue', scale_units='xy', scale=1, alpha=1)

    # Example new vectors (replace with your actual new vectors)
    # new_vec1 = np.array([3, -1])
    # new_vec2 = np.array([2, 3])

    # Find lengths of the original vectors
    # length_b1 = np.linalg.norm(b1)
    # length_b2 = np.linalg.norm(b2)

    # Normalize the new vectors (scale them to unit length)
    # new_vec1_normalized = new_vec1 / np.linalg.norm(new_vec1)
    # new_vec2_normalized = new_vec2 / np.linalg.norm(new_vec2)

    # Scale the new vectors to have the same length as b1 and b2
    # new_vec1_scaled = new_vec1_normalized * length_b1
    # new_vec2_scaled = new_vec2_normalized * length_b2
    # ax.quiver(0, 0, new_vec1_scaled[0], new_vec1_scaled[1], color='red', scale_units='xy', scale=1, alpha=0.25)
    # ax.quiver(0, 0, new_vec2_scaled[0], new_vec2_scaled[1], color='blue', scale_units='xy', scale=1, alpha=0.25)
    # ax.quiver(0, 0, new_vec1[0], new_vec1[1], color='red', scale_units='xy', scale=1, alpha=0.25)
    # ax.quiver(0, 0, new_vec2[0], new_vec2[1], color='blue', scale_units='xy', scale=1, alpha=0.25)
    ax.scatter(target[0] - e[0], target[1] - e[1], color='green', linewidths=5, alpha=1)
    ax.scatter(target[0], target[1], color='red', linewidths=5, alpha=1)
    for p in points:
        # Calculate the center offset
        center_offset = (b1 + b2) / 2
        # Define vertices for the parallelepiped centered on the lattice point
        vertices = [p - center_offset, p - center_offset + b1, p - center_offset + b1 + b2, p - center_offset + b2]
        path = Path(vertices)
        if path.contains_point(np.array([target[0] - e[0], target[1] - e[1]])):
            fill_color = 'yellow'
            fill_alpha = 0.3
        else:
            fill_color = 'none'
            fill_alpha = 0.3
        parallelepiped = patches.Polygon(vertices, closed=True, fill=True, edgecolor=color, linewidth=linewidth, alpha=fill_alpha, facecolor=fill_color)
        ax.add_patch(parallelepiped)


if __name__ == '__main__':
    
    # Define original basis
    b1 = np.array([1, 0])
    b2 = np.array([0.5, np.sqrt(3)/2])
    basis_vectors = [b1, b2]

    # Define a "bad" basis
    bad_b1 = np.array([5/2, np.sqrt(3)/2])
    bad_b2 = np.array([2, np.sqrt(3)])
    bad_basis_vectors = [bad_b1, bad_b2]

    bad_voronoi = [bad_b2, b2]

    # define the plotting area
    ldown = np.array([-3, -3])
    rup = np.array([3, 3])

    theta = np.radians(95)  # 45 degree rotation
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])


    # Rotate both basis vectors
    rotated_b1 = rotation_matrix @ b1
    rotated_b2 = rotation_matrix @ b2
    rotated_basis_vectors = [rotated_b1, rotated_b2]

    target_point = np.array([-3/2, np.sqrt(3)/2])
    e = [-0.25, 0.13]
    rotated_target_point = rotation_matrix @ target_point
    rot_e = rotation_matrix @ e

    bad_rot_1 = rotation_matrix @ bad_b1
    bad_rot_2 = rotation_matrix @ bad_b2
    bad_rot_voronoi = [bad_rot_2, rotated_b2]

    fig, ax = plt.subplots()
    points = plotLattice(ax, rotated_basis_vectors, ldown, rup, 'blue', 3, 1)
    # plotParallelepipeds(ax, bad_rot_voronoi, points, 'green', 1, 0.25, rotated_target_point, rot_e)

    # resize the plotting window
    mngr = plt.get_current_fig_manager()
    # mngr.resize(960, 1080)
    
    # tune axis
    ax.set_aspect('equal')
    ax.grid(False)
    ax.set_xlim(ldown[0], rup[0])
    ax.set_ylim(ldown[1], rup[1])

# Hide axis but keep the grid
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)    
    # ax.scatter(rotated_target_point[0] - e[0], rotated_target_point[1] - e[1], color='green', linewidths=5, alpha=0.25)
    # ax.scatter(rotated_target_point[0], rotated_target_point[1], color='red', linewidths=5, alpha=0.25)
    ax.quiver(0, 0, bad_rot_1[0], bad_rot_1[1], color='red', scale_units='xy', scale=1, alpha=1)
    ax.quiver(0, 0, bad_rot_2[0], bad_rot_2[1], color='blue', scale_units='xy', scale=1, alpha=1)
    # show the plot
    plt.show()
