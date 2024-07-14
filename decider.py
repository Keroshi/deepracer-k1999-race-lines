import numpy as np
import matplotlib.pyplot as plt

track = np.load("tracks/reInvent2019_track.npy")
race_line = np.load("racelines/reInvent2019_track-1000-4-2019-11-09-113228.npy")

# Extract only the x and y coordinates of the track points (first two columns)
track_points = track[:, :2]

left_lane_classification = []
center_lane_classification = []
right_lane_classification = []


# Function to classify points into lanes
def classify_points(track_points, race_line_points):
    left_lane = []
    center_lane = []
    right_lane = []

    counter = 0

    for point in race_line_points:
        # Find the closest point on the track to the current race line point
        distances = np.linalg.norm(track_points - point, axis=1)
        closest_point_index = np.argmin(distances)
        closest_point = track_points[closest_point_index]

        # Determine if the point is left, center, or right
        if point[0] < closest_point[0]:  # Adjust based on your track orientation
            left_lane.append(point)
            left_lane_classification.append(counter)
        elif point[0] > closest_point[0]:
            right_lane.append(point)
            right_lane_classification.append(counter)
        else:
            center_lane.append(point)
            center_lane_classification.append(counter)

        counter += 1

    return np.array(left_lane), np.array(center_lane), np.array(right_lane)


# Classify the race line points into lanes
left_lane, center_lane, right_lane = classify_points(track_points, race_line)

# Plotting
plt.figure(figsize=(10, 7))
plt.scatter(track_points[:, 0], track_points[:, 1], color='cyan', s=10, label="Track")
if len(left_lane) > 0:
    plt.scatter(left_lane[:, 0], left_lane[:, 1], color='blue', s=10, label="Left Lane")
if len(center_lane) > 0:
    plt.scatter(center_lane[:, 0], center_lane[:, 1], color='green', s=10, label="Center Lane")
if len(right_lane) > 0:
    plt.scatter(right_lane[:, 0], right_lane[:, 1], color='red', s=10, label="Right Lane")

plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.legend()
plt.title("Track with Classified Lanes")
plt.grid(True)
plt.show()

print(left_lane_classification)
print(center_lane_classification)
print(right_lane_classification)
