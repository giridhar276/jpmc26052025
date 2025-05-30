
#Write a program to print team names and player names.

teams = {
    "TeamA": [
        {"name": "Alice", "role": "Batsman"},
        {"name": "Bob", "role": "Bowler"}
    ],
    "TeamB": [
        {"name": "Charlie", "role": "Allrounder"},
        {"name": "Dave", "role": "Wicketkeeper"}
    ]
}

for team,playerinfo in teams.items():
    print("Team name :",team)
    print("------------")
    for player in playerinfo:
        print(player['name'])