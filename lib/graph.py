import math

class CityGraph:
    def __init__(self):
        self.adj_matrix = []
        self.cities = {}

    def routing(self):
        # Agha Reza to inja benvis
        pass
    
    def range_query(self):
        # Hanie to inja benvis
        pass
    

    def insert_new_city(self, city_name, population, coordinates):
        
        self.cities[city_name] = {'population': population, 'coordinates': coordinates}

        distances = [self.calculate_distance(coordinates, self.cities[other_city]['coordinates']) for other_city in self.cities]
        
        for i, row in enumerate(self.adj_matrix):
            row.append(distances[i])
        self.adj_matrix.append(distances + [0])

    @staticmethod
    def calculate_distance(coord1, coord2):
        return round(math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2), 1)
    