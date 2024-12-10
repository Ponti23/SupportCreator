import numpy as np
import trimesh

"""
# Step 1: Create a 2D triangle
# Define the 3 vertices of the triangle
L1 = 2
L2 = 1
L3 = 10
L4 = 10
R1 = 2
R2 = 1
R3 = 0.5

# Define vertices
vertices = np.array([
    [0, 0],  # Bottom-left
    [R1, 0],  # Bottom-right
    [R1, L1],  # Top-right of first segment
    [R2, L3 - L2],  # Bottom-right of next segment
    [R2, L3],  # Top-right of second segment
    [R3, L3],  # Bottom-right of final segment
    [R3, L3+L4],  # Top-right of final segment
    [0, L3+L4],  # Top-left
    [0, 0]  # Close the shape
])

"""

def build_shape(vertices):
    divisions = 50
    angles = np.linspace(0, 2 * np.pi, divisions)
    cone_vertices = []

    for angle in angles:
        rotation_matrix = np.array([
            [np.cos(angle), 0, np.sin(angle)],  # Rotation around Y-axis
            [0, 1, 0],
            [-np.sin(angle), 0, np.cos(angle)]
        ])
        
        for vertex in vertices:
            rotated_vertex = np.dot(rotation_matrix, np.append(vertex, 0))  # Add z=0 for 2D rotation
            cone_vertices.append(rotated_vertex)
        
    cone_vertices = np.array(cone_vertices)

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
    return cone_mesh