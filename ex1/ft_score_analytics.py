import sys

print("=== Player Score Analytics ===")
scores_list: list[int] = []
for x_str in sys.argv[1:]:
    try:
        x_int = int(x_str)
        scores_list.append(x_int)
    except ValueError:
        print(f"Invalid parameter: '{x_str}'")
if scores_list == []:
    print("No scores provided.", end=" ")
    print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
else:
    print(f"Scores processed: {scores_list}")
    print(f"Total players: {len(scores_list)}")
    print(f"Total score: {sum(scores_list)}")
    print(f"Average score: {sum(scores_list) / len(scores_list)}")
    print(f"High score: {max(scores_list)}")
    print(f"Low score: {min(scores_list)}")
    print(f"Score range: {max(scores_list) - min(scores_list)}")
