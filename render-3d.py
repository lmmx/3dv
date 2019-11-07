from stl import mesh
from mpl_toolkits.mplot3d import Axes3D, art3d
from matplotlib import pyplot as plt

# Create a new plot
fig = plt.figure()
ax = Axes3D(fig)

# Load the STL files and add the vectors to the plot
#m = mesh.Mesh.from_file('HalfDonut.stl')
#m = mesh.Mesh.from_file('stl/Labs_septic.stl')
m = mesh.Mesh.from_file('stl/Sarti_surface.stl')

ax.add_collection3d(art3d.Poly3DCollection(m.vectors))

# Auto scale to the mesh size
scale = m.points.flatten('F')
ax.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
plt.show()
