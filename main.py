from lib.graph import CityGraph
from lib.file_worker import *
import os
import time

def main():
    
    graph = CityGraph()
    graph.cities = load_cities_from_json()
    num_cities = len(graph.cities)
    graph.adj_matrix = load_matrix_from_csv()

    while True:
        
        os.system('clear' if os.name == 'posix' else 'cls')
        
        print("\033[1;36mMenu: \033[0m")
        print("1- Routing")
        print("2- Range Query")
        print("3- Insert a new city")
        print("4- Exit")
        choice = input("\033[1;36mEnter your choice: \033[0m")

        if choice == '1':
            origin = input("origin city name: ")
            destination = input("destination city name: ")
            graph.routing(origin, destination)
            input("press Enter to continue...")
             
        
        elif choice == '2':
            # Hanie to inja benvis
            pass
        
        elif choice == '3':
            city_name = input("Enter city name: ")
            population = int(input("Enter population: "))
            coordinates = tuple(map(int, input("Enter coordinates (x y): ").split()))
            graph.insert_new_city(city_name, population, coordinates)
            save_cities_to_json(graph.cities)
            save_matrix_to_csv(graph.adj_matrix)
            print("\033[1;32m--Your city has been successfully registered--")
            time.sleep(3)
            
        elif choice == '4':
            break
        
        else:
            print("\033[1;31mInvalid choice. Please enter a number between 1 and 4. \033[0m")
            time.sleep(2.5)

if __name__ == "__main__":
    main()