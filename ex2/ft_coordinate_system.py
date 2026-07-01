import math


def get_player_pos() -> tuple[float, float, float]:
    retry: bool = True
    while retry:
        retry = False
        str_input: str = input(
            "Enter new coordinates as floats in format 'x, y, z': "
            )
        str_list: list[str] = str_input.split(",")
        if len(str_list) != 3:
            print("Invalid syntax")
            retry = True
        else:
            for i in range(3):
                try:
                    float(str_list[i])
                except Exception as err:
                    print(f"Error on parameter '{str_list[i]}': {err}")
                    retry = True
    my_tuple: tuple[float, float, float] = (
        float(str_list[0]), float(str_list[1]), float(str_list[2])
        )
    return my_tuple


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    coords: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {coords}")
    print(f"It includes: X={coords[0]}, Y={coords[1]}, Z={coords[2]}")
    distance: float = math.sqrt(
        (coords[0] - 0)**2 +
        (coords[1] - 0)**2 +
        (coords[2] - 0)**2
        )
    print(f"Distance to center: {round(distance, 4)}")
    print("\nGet a second set of coordinates")
    coords2: tuple[float, float, float] = get_player_pos()
    distance = math.sqrt(
        (coords[0] - coords2[0])**2 +
        (coords[1] - coords2[1])**2 +
        (coords[2] - coords2[2])**2
        )
    print(
        f"Distance between the two sets of coordinates: {round(distance, 4)}"
        )
