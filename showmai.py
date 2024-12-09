import pyvista as pv  # Correct import for PyVista
import streamlit as st
from stpyvista import stpyvista

# Streamlit app title
st.title("PyVista with Streamlit Example")
st.subheader("Interactive 3D Sphere Visualization")

# Description
st.write(
    """
    This example demonstrates how to integrate PyVista with Streamlit to render 
    3D geometries. The visualization below shows a sphere with a scalar field applied.
    """
)

# Initialize a PyVista plotter
plotter = pv.Plotter(window_size=[600, 600])

# Create a sphere mesh
sphere = pv.Sphere(radius=1.0, center=(0, 0, 0), theta_resolution=30, phi_resolution=30)

# Add a scalar field (e.g., based on Z-coordinates of the points)
sphere["Z-coordinates"] = sphere.points[:, 2]

# Add the sphere mesh to the plotter with the scalar field
plotter.add_mesh(
    sphere,
    scalars="Z-coordinates",
    cmap="viridis",  # Color map
    show_scalar_bar=True,
)

# Set camera view and background color
plotter.view_isometric()
plotter.background_color = "white"

# Render the plotter in Streamlit
stpyvista(plotter, key="pyvista_sphere")

# Add a footer
st.write("Rendered using PyVista and Streamlit!")
