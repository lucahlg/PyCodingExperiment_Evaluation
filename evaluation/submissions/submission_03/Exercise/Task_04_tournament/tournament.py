def tally(rows):
    from collections import defaultdict

    # Initialize team statistics
    stats = defaultdict(lambda: {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0})

    # Process each match result
    for row in rows:
        team1, team2, result = row.split(';')
        stats[team1]["MP"] += 1
        stats[team2]["MP"] += 1

        if result == "win":
            stats[team1]["W"] += 1
            stats[team1]["P"] += 3
            stats[team2]["L"] += 1
        elif result == "loss":
            stats[team2]["W"] += 1
            stats[team2]["P"] += 3
            stats[team1]["L"] += 1
        elif result == "draw":
            stats[team1]["D"] += 1
            stats[team2]["D"] += 1
            stats[team1]["P"] += 1
            stats[team2]["P"] += 1

    # Sort teams by points and name
    sorted_teams = sorted(stats.items(), key=lambda x: (-x[1]["P"], x[0]))

    # Format the output table
    output = ["Team                           | MP |  W |  D |  L |  P"]
    for team, stat in sorted_teams:
        output.append(f"{team:30} | {stat['MP']:2} | {stat['W']:2} | {stat['D']:2} | {stat['L']:2} | {stat['P']:2}")

    return "\n".join(output)
