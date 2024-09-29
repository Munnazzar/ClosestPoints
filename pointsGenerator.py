import csv
import random

# Generate 1 million random 3D points with values ranging from -10 to 10
points = [(random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(5_000)]

# Save to a CSV file
csv_file_path = '1_million_points.csv'
with open(csv_file_path, mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(points)

csv_file_path
