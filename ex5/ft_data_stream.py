#!/usr/bin/env python3
import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    list_names: list[str] = ['bob', 'alice', 'dylan', 'charlie']
    list_actions: list[str] = [
        'run', 'eat', 'sleep', 'grab', 'move', 'climb', 'swim', 'release'
        ]
    name: str = random.choice(list_names)
    action: str = random.choice(list_actions)
    t_event: tuple[str, str] = (name, action)

    yield t_event


def consume_event(l_tuples: list[tuple[str, str]]) -> typing.Generator[
        tuple[str, str], list[tuple[str, str]], None
        ]:
    l_element: tuple[str, str] = random.choice(l_tuples)
    l_tuples.remove(l_element)

    yield l_element


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        gen_tuple = next(gen_event())
        print(f"Event {i}: Player {gen_tuple[0]} did action {gen_tuple[1]}")

    l_tuples: list[tuple[str, str]] = []
    for i in range(10):
        l_tuples.append(next(gen_event()))
    print("\nBuilt list of 10 events:", l_tuples)
    for i in range(10):
        print("Got event from list: ", next(consume_event(l_tuples)))
        print("Remains in list: ", l_tuples)
