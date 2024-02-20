houses_seed_count = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

playing = True

player_one = True

message_code = 0

while playing:

    if player_one and message_code == 0:
        message = "Player One... you're up!"
    elif not player_one and message_code == 0:
        message = "Player Two... you're up!"
    elif player_one and message_code == -1:
        message = "Invalid input. Have another go, Player One."
    elif not player_one and message_code == -1:
        message = "Invalid input. Have another go, Player Two."
    elif player_one and message_code == -2:
        message = "You must choose a house with seeds, Player One. Try again."
    elif not player_one and message_code == -2:
        message = "You must choose a house with seeds, Player Two. Try again."
    print("")
    print(message)
    message_code = 0

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

    user_input = input("Enter a letter to choose the corresponding house or enter 'exit' to leave the game: ")

    if user_input == "exit":
        playing = False
        selected_house = 0
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
    else:
        message_code = -1
        selected_house = -1 
    
    if selected_house >= 0:
        seeds = houses_seed_count[selected_house]
        if int(seeds) == 0:
            message_code = -2
            continue

        houses_seed_count[selected_house] = 0
            
        current_house = selected_house
        while int(seeds) > 0:
            current_house += 1
            if current_house == 6:  
                current_house = 7
            elif current_house == 13:  
                current_house = 0

            houses_seed_count[current_house] = int(houses_seed_count[current_house]) + 1
            seeds = int(seeds) - 1

        if player_one:
            opponent_houses_range = range(7, 13)  
        else:
            opponent_houses_range = range(0, 6)  

        if current_house in opponent_houses_range and houses_seed_count[current_house] in [2, 3]:
            if player_one:
                houses_seed_count[6] = int(houses_seed_count[6]) + houses_seed_count[current_house]
            else:
                houses_seed_count[13] = int(houses_seed_count[13]) + houses_seed_count[current_house]
            houses_seed_count[current_house] = 0

        player_one = not player_one  