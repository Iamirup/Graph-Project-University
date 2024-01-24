import json
import csv

def save_cities_to_json(cities, filename="database/cities.json"):
    with open(filename, 'w') as f:
        json.dump(cities, f, indent=4)

def load_cities_from_json(filename="database/cities.json"):
    with open(filename, 'r') as f:
        return json.load(f)

def save_matrix_to_csv(matrix, filename="database/matrix.csv"):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(matrix)

def load_matrix_from_csv(filename="database/matrix.csv"):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return [list(map(float, row)) for row in reader]