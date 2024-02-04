houses_seed_count = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

playing = True

player_one = True

while playing:

    if player_one:
        message = "Player One... you're up!"
    else:
        message = "Player Two... you're up!"
    print("")
    print(message)

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
    elif player_one and user_input == "a":
        selected_house = 5
    elif player_one and user_input == "b":
        selected_house = 4
    elif player_one and user_input == "c":
        selected_house = 3
    elif player_one and user_input == "d":
        selected_house = 2
    elif player_one and user_input == "e":
        selected_house = 1
    elif player_one and user_input == "f":
        selected_house = 0
    elif not player_one and user_input == "a":
        selected_house = 12
    elif not player_one and user_input == "b":
        selected_house = 11
    elif not player_one and user_input == "c":
        selected_house = 10
    elif not player_one and user_input == "d":
        selected_house = 9
    elif not player_one and user_input == "e":
        selected_house = 8
    elif not player_one and user_input == "f":
        selected_house = 7

    houses_seed_count[selected_house] = 0

    player_one = not player_one