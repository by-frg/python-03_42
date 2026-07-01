import sys


inventory: dict[str,int] = {}
if len(sys.argv) == 1:
    print("Error: No arguments received. Your inventory is empty.")
else:
    for i in range(1, len(sys.argv)):
        try:
            colon: int = sys.argv[i].index(":")
        except Exception:
            print(f"Error - Invalid parameter '{sys.argv[i]}'")
            continue
        inv_key: str = sys.argv[i][:colon]
        try:
            inv_value: int = int(sys.argv[i][colon + 1:])
        except Exception as err:
            print(f"Quantity error for '{inv_key}': {err}")
            continue
        try:
            inventory.update({inv_key:inv_value})
        except Exception as err:
            print(err)
print(inventory)
## como detetar valor repetido (corretamente ignorado?)
