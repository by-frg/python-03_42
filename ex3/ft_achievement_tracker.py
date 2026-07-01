import random


def gen_player_achievements() -> set[str]:
    l_achiev: list[str] = [
        'Crafting Genius',
        'World Savior',
        'Master Explorer',
        'Collector Supreme',
        'Untouchable',
        'Boss Slayer',
        'Strategist',
        'Unstoppable',
        'Speed Runner',
        'Survivor',
        'Treasure Hunter',
        'First Steps',
        'Sharp Mind'
        ]
    elements: int = random.randint(5, len(l_achiev) - 1)
    player_set: set[str] = set(random.sample(l_achiev, elements))
    return player_set


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    player1: set[str] = gen_player_achievements()
    player2: set[str] = gen_player_achievements()
    player3: set[str] = gen_player_achievements()
    player4: set[str] = gen_player_achievements()
    print(f"Player Alice: {player1}")
    print(f"Player Bob: {player2}")
    print(f"Player Charlie: {player3}")
    print(f"Player Dylan: {player4}")
    s_union: set[str] = set.union(player1, player2, player3, player4)
    print(f"\nAll distinct achievements: {s_union}")
    s_shared: set[str] = set.intersection(player1, player2, player3, player4)
    print(f"\nCommon achievements: {s_shared}\n")
    p1_diff: set[str] = player1.difference(player2, player3, player4)
    print(f"Only Alice has: {p1_diff}")
    p2_diff: set[str] = player2.difference(player1, player3, player4)
    print(f"Only Bob has: {p2_diff}")
    p3_diff: set[str] = player3.difference(player1, player2, player4)
    print(f"Only Charlie has: {p3_diff}")
    p4_diff: set[str] = player4.difference(player1, player2, player3)
    print(f"Only Charlie has: {p4_diff}")
    print(f"\nAlice is missing: {s_union - player1}")
    print(f"Bob is missing: {s_union - player2}")
    print(f"Charlie is missing: {s_union - player3}")
    print(f"Dylan is missing: {s_union - player4}")
