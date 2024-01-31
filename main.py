from lib.graph import CityGraph
from lib.file_worker import *
import time
import os

def main():
    
    graph = CityGraph()
    graph.cities = load_cities_from_json()
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
            origin = input("Origin city name: ")
            destination = input("Destination city name: ")
            
            start_time = time.time()
            graph.routing(origin, destination)
            end_time = time.time()
            
            print(f"Execution time: \033[1;32m{end_time - start_time}\033[0m seconds")
            input("press Enter to continue...")
                     
        elif choice == '2':
            population1 = int(input("Enter the first population: "))
            population2 = int(input("Enter the second population: "))
            
            start_time = time.time()
            for i,j in graph.range_query(population1,population2):
                print(f"\033[1;32m{i}\033[0m with \033[1;32m{j}\033[0m population is between the two populations that you selected.")
            end_time = time.time()
            
            print(f"Execution time: \033[1;32m{end_time - start_time}\033[0m seconds")
            input("press Enter to continue...")
        
        elif choice == '3':
            city_name = input("Enter city name: ")
            population = int(input("Enter population: "))
            coordinates = tuple(map(int, input("Enter coordinates (x y): ").split()))
            
            start_time = time.time()
            graph.insert_new_city(city_name, population, coordinates)
            end_time = time.time()
            
            save_cities_to_json(graph.cities)
            save_matrix_to_csv(graph.adj_matrix)
            print("\033[1;32m--Your city has been successfully registered--\033[0m")
            print(f"Execution time: \033[1;32m{end_time - start_time}\033[0m seconds")
            input("press Enter to continue...")
            
        elif choice == '4':
            break
        
        else:
            print("\033[1;31mInvalid choice. Please enter a number between 1 and 4. \033[0m")
            input("press Enter to continue...")

if __name__ == "__main__":
    main()