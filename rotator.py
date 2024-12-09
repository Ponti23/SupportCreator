import numpy as np
import trimesh

# Step 1: Create a 2D triangle
# Define the 3 vertices of the triangle
vertices = np.array([
    [0, 0],  
    [2, 0],  
    [2, 2],  
    [1, 9],  
    [1, 10],  
    [0.5, 10],  
    [0.5, 20],  
    [0, 20],
    [0, 0]
])

# Step 2: Revolve the triangle around the Y-axis (for a cone)
# Number of divisions for the revolution (more divisions = smoother cone)
divisions = 50
angles = np.linspace(0, 2 * np.pi, divisions)

# Step 3: Create the cone by rotating the triangle around the Y-axis
# Initialize an empty list to store the cone vertices
cone_vertices = []

# Revolve each triangle vertex around the Y-axis
for angle in angles:
    rotation_matrix = np.array([
        [np.cos(angle), 0, np.sin(angle)],  # Rotation around Y-axis
        [0, 1, 0],
        [-np.sin(angle), 0, np.cos(angle)]
    ])
    
    # Apply rotation to each vertex
    for vertex in vertices:
        rotated_vertex = np.dot(rotation_matrix, np.append(vertex, 0))  # Add z=0 for 2D rotation
        cone_vertices.append(rotated_vertex)
    
# Convert cone_vertices to a numpy array
cone_vertices = np.array(cone_vertices)

# Step 4: Create faces for the cone
# Each triangle will have vertices connecting to the center (for the cone sides)
faces = []
center_index = len(vertices) * divisions  # The center of the cone (not actually a vertex, but the axis of revolution)

# Create faces for each section
for i in range(divisions - 1):
    for j in range(len(vertices) - 1):
        faces.append([
            i * len(vertices) + j,
            i * len(vertices) + (j + 1) % len(vertices),
            (i + 1) * len(vertices) + j
        ])
        faces.append([
            i * len(vertices) + (j + 1) % len(vertices),
            (i + 1) * len(vertices) + (j + 1) % len(vertices),
            (i + 1) * len(vertices) + j
        ])

# Convert faces to numpy array
faces = np.array(faces)

# Step 5: Create the mesh using trimesh
cone_mesh = trimesh.Trimesh(vertices=cone_vertices, faces=faces)

# Step 6: Show the cone
cone_mesh.show()
