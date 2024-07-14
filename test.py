# import os
# import numpy as np
#
# # Specify the directory containing the files
# folder_path = 'C:\\Users\\User\\DataspellProjects\\deepracer-k1999-race-lines\\tracks'
#
# array = []
#
# # Iterate over files in the directory
# for filename in os.listdir(folder_path):
#     file = np.load(f"C:\\Users\\User\\DataspellProjects\\deepracer-k1999-race-lines\\tracks\\{filename}")
#     array.append([filename, len(file)])
#
# for item in sorted(array, key=lambda x: x[1]):
#     print(item)


import numpy as np

# Sample arrays
point = np.array([1.72003921, -5.12926025])
track_points = np.array([1.726677, -5.1060586, 1.85320401, -4.58788204, 1.60014999, -5.62423515])

# Extract center, left, and right points
center = track_points[:2]
left = track_points[2:4]
right = track_points[4:]


# Function to calculate Euclidean distance
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))


# Calculate distances
distance_center = euclidean_distance(point, center)
distance_left = euclidean_distance(point, left)
distance_right = euclidean_distance(point, right)

# Compare distances
distances = {
    'center': distance_center,
    'left': distance_left,
    'right': distance_right
}

# Determine the closest point
closest_point = min(distances, key=distances.get)

print(f"Distances: {distances}")
print(f"Closest point: {closest_point}")
