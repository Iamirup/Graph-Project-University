import math
import heapq



class CityGraph:
    def __init__(self):
        self.adj_matrix = []
        self.cities = {}

    def _get_neighbors(self, city):
         if city not in self.cities:
            return []

         index = list(self.cities.keys()).index(city)
         if index >= len(self.adj_matrix):
            return []

         for i, distance in enumerate(self.adj_matrix[index]):
            if i < len(self.cities) and distance > 0:
                yield list(self.cities.keys())[i], distance

    def routing(self, origin, destination):
        if origin not in self.cities or destination not in self.cities:
            print("Origin or destination city not found.")
            return

        distances = {city: float('inf') for city in self.cities}
        distances[origin] = 0
        previous = {city: None for city in self.cities}

        priority_queue = [(0, origin)]

        while priority_queue:
            current_distance, current_city = heapq.heappop(priority_queue)

            if current_distance > distances[current_city]:
                continue

            for neighbor, distance in self._get_neighbors(current_city):
                new_distance = current_distance + distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_city
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        path = []
        current_city = destination
        while current_city:
            path.insert(0, current_city)
            current_city = previous[current_city]

        if path[0] == origin:
            print("Shortest path:", " -> ".join(path), "Total distance:", distances[destination])
        else:
            print("There is no route between the origin and destination cities.")
        
    
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