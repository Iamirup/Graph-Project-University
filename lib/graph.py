class CityGraph:
    def __init__(self):
        self.adj_matrix = []
        self.cities = {}

    def routing(self, origin, destination):
        
        if origin not in self.cities and destination not in self.cities:
            print("\033[1;31mOrigin and destination city not found.\033[0m")
            return
        if origin not in self.cities:
            print("\033[1;31mOrigin city not found.\033[0m")
            return
        if destination not in self.cities:
            print("\033[1;31mDestination city not found.\033[0m")
            return

        distances = {city: float('inf') for city in self.cities}
        distances[origin] = 0
        unvisited = set(self.cities.keys())
        previous = {city: None for city in self.cities}
        
        while unvisited:
            current_city = min(unvisited, key=distances.get)
            unvisited.remove(current_city)

            if distances[current_city] == float('inf'):
                break

            for neighbor, distance in self._get_neighbors(current_city):
                new_distance = distances[current_city] + distance
                
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_city
                    
        path = []
        current_city = destination
        while current_city:
            path.insert(0, current_city)
            current_city = previous[current_city]

        if path[0] == origin:
            print("\033[1;32mShortest path:\033[0m", " -> ".join(path), "\n\033[1;32mTotal distance:\033[0m", distances[destination])
        else:
            print("\033[1;31mThere is no route between the origin and destination cities.\033[0m")
    
    def range_query(self, a, b):
        found = False
        for city, data in self.cities.items():
            population = data['population']
            population = int(population)
            if a <= population <= b:
                yield city, population
                found = True
        if not found:
            print(f"\033[1;31mNo city with population between {a} and {b} was found!\033[0m")

    def insert_new_city(self, city_name, population, coordinates):
        
        distances = [self._calculate_distance(coordinates, self.cities[other_city]['coordinates']) for other_city in self.cities]
        
        self.cities[city_name] = {'population': population, 'coordinates': coordinates}
          
        l = len(self.adj_matrix)
        
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0] * (l+1))
        
        nearest = sorted((range(l)), key=lambda i: distances [i])[:3]

        for i in nearest:
            weight = distances[i]
            self.adj_matrix[i][l] = weight
            self.adj_matrix[l][i] = weight        

        for i in range(l):
            if i not in nearest:
                self.adj_matrix[i][l] = float('inf')
                self.adj_matrix[l][i] = float('inf')
                
    def _get_neighbors(self, city):
        if city not in self.cities:
            return []

        index = list(self.cities.keys()).index(city)
        if index >= len(self.adj_matrix):
            return []

        for i, distance in enumerate(self.adj_matrix[index]):
           if i < len(self.cities) and distance > 0:
             yield list(self.cities.keys())[i], distance

    def _calculate_distance(self, coord1, coord2):
        return round(((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)**0.5, 1)
    