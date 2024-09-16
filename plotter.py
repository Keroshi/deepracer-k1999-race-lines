import numpy as np
import matplotlib.pyplot as plt

# Load the track and race line data
track = np.load("tracks/Austin.npy")
race_line = np.load("racelines/Austin-1000-4-2024-09-13-110627.npy")

# Extract x and y coordinates for left, center, and right lanes from the track data
x_coords = track[:, [0, 2, 4]].flatten()
y_coords = track[:, [1, 3, 5]].flatten()

# Plotting
plt.figure(figsize=(12, 8))

# Plot track points
plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='blue', markersize=2, label="Track")

# Plot race line points with indices
plt.scatter(race_line[:, 0], race_line[:, 1], color='red', s=10, label="Race Line")
for idx, (x, y) in enumerate(race_line):
    plt.text(x, y, str(idx), fontsize=8, color='red')

# Adding labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Track Plot with Race Line')

# Invert y-axis to match typical coordinate system (optional)
plt.gca()
plt.grid(True)  # Add grid (optional)
plt.legend()
plt.show()

# Print specific points for debugging purposes
print(track[37])
print(race_line[37])
