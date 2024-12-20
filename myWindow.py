import trimesh
import pyglet
from pyglet.gl import *

# Load a trimesh object
mesh = trimesh.load("test.stl")

# Create a trimesh Scene
scene = trimesh.Scene(mesh)

# Define a custom viewer with culling enabled
class CustomViewer(trimesh.viewer.SceneViewer):
    def on_draw(self):
        # Enable back-face culling
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)  # Cull back faces (default)
        super().on_draw()

# Open the viewer with the custom configuration
viewer = CustomViewer(scene=scene)
pyglet.app.run()
