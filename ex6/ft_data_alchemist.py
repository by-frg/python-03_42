#!/usr/bin/env python3
import random

print("=== Game Data Alchemist ===\n")
l_players: list[str] = ['Alice', 'bob', 'Charlie', 'dylan',
                        'Emma', 'Gregory', 'john', 'kevin', 'Liam']
all_players: list[str] = [player.capitalize() for player in l_players]
cap_players: list[str] = [
    player for player in l_players if (player == player.capitalize())
    ]
print("Initial list of players: ", l_players)
print("New list with all names capitalized: ", all_players)
print("New list of capitalized names only: ", cap_players)
print()

d_scores: dict[str, int] = {x: random.randint(1, 1000) for x in all_players}
print("Score dict: ", d_scores)
avg_score = sum(d_scores.values()) / len(d_scores)
print(f"Score average is {round(avg_score, 1)}")
d_highscores: dict[str, int] = {
    player: score for player, score in d_scores.items() if score > avg_score
    }
print("High scores: ", d_highscores)
