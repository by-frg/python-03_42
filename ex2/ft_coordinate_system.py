import sys
import math

def get_player_pos() -> tuple():
    retry: bool = True
    while retry:
        retry: bool = False
        str_input: str = input("Enter new coordinates as floats in format 'x, y, z': ")
        str_list: list[str] = str_input.split(",")
        try:
            coord1: float = float(str_list[0])
            coord2: float = float(str_list[1])
            coord3: float = float(str_list[2])
        except (ValueError, IndexError):
            print("Invalid syntax")
            retry = True
    my_tuple: tuple(float) = (coord1, coord2, coord3)
    return(my_tuple)

if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    coordinates: tuple() = get_player_pos()
    print(f"Got a first tuple: {coordinates}")
    print(f"It includes: X={coordinates[0]}, Y={coordinates[1]}, Z={coordinates[2]}")
    #calculo distancia
    #rever handle de erros e msg que passa


    
    
