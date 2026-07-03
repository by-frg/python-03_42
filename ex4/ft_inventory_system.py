#!/usr/bin/env python3
import sys


inventory: dict[str, int] = {}
if len(sys.argv) == 1:
    print("Error: No arguments received. Your inventory is empty.")
else:
    print("=== Inventory System Analysis ===")
    for i in range(1, len(sys.argv)):
        try:
            colon: int = sys.argv[i].index(":")
        except Exception:
            print(f"Error - invalid parameter '{sys.argv[i]}'")
            continue
        inv_key: str = sys.argv[i][:colon]
        if inv_key in inventory:
            print(f"Redundant item'{inv_key}' - discarding")
            continue
        try:
            inv_value: int = int(sys.argv[i][colon + 1:])
        except Exception as err:
            print(f"Quantity error for '{inv_key}': {err}")
            continue
        inventory.update({inv_key: inv_value})

    print(f"Got inventory: {inventory}")
    item_list: list[str] = list(inventory.keys())
    print(f"Item list: {item_list}")
    qty_list: list[int] = list(inventory.values())
    print(f"Total quantity of the {len(item_list)} item(s): {sum(qty_list)}")

    for x in inventory:
        print(f"Item {x} represents "
              f"{round(inventory[x] / sum(qty_list) * 100, 1)}%")
    max_i: int = 0
    for i in range(1, len(qty_list)):
        if (qty_list[max_i] > qty_list[i]):
            continue
        else:
            max_i = i
    print(f"Item most abundant: "
          f"{item_list[max_i]} with quantity {qty_list[max_i]}")
    min_i: int = 0
    for i in range(1, len(qty_list)):
        if (qty_list[min_i] < qty_list[i]):
            continue
        else:
            min_i = i
    print(f"Item least abundant: "
          f"{item_list[min_i]} with quantity {qty_list[min_i]}")
    inventory.update({'magic_item': 1})
    print(f"Updated inventory: {inventory}")
