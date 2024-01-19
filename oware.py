houses_seed_count = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

playing = True

player_one = True

while playing:

    for i in range(0, len(houses_seed_count)):
        houses_seed_count[i] = int(houses_seed_count[i])
        if houses_seed_count[i] < 10:
            houses_seed_count[i] = " " + str(houses_seed_count[i])

    print("")
    if not player_one:
        print("        a    b    c    d    e    f")
    print("+----+----+----+----+----+----+----+----+")
    print(f"|    | {houses_seed_count[12]} | {houses_seed_count[11]} | {houses_seed_count[10]} | {houses_seed_count[9]} | {houses_seed_count[8]} | {houses_seed_count[7]} |    |")
    print(f"| {houses_seed_count[13]} |----+----+----+----+----+----| {houses_seed_count[6]} |")
    print(f"|    | {houses_seed_count[0]} | {houses_seed_count[1]} | {houses_seed_count[2]} | {houses_seed_count[3]} | {houses_seed_count[4]} | {houses_seed_count[5]} |    |")
    print("+----+----+----+----+----+----+----+----+")
    if player_one:
        print("        f    e    d    c    b    a")
    print("")

    user_input = input("Enter 'exit' to leave the game: ")

    if user_input == "exit":
        playing = False

    player_one = not player_one