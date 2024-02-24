houses_seed_count = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

playing = True

player_one = True

message_code = 0

print("-------------------------------------------------Welcome to Oware!------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------Instructions---------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------------------------------")
print("1. Players take turns to select a house to distribute seeds anti-clockwise.")
print("2. If the last seed lands in an opponent's house that then has 2 or 3 seeds, those seeds are captured.")
print("3. Additionally, if any preceding houses on the opponent's side also have exactly 2 or 3 seeds, those seeds are also captured.")
print("4. The game ends when a player cannot play a turn. Remaining seeds go to the opponent.")
print("5. The player with the most seeds in their store at the end wins.")
print("6. Enter 'a' to 'f' to select a house, or 'exit' to end the game.")
print("------------------------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------Let's start the game!----------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------------------------------")

while playing:

    if player_one:
        player_houses = houses_seed_count[0:6] 
        opponent_houses = houses_seed_count[7:13] 
        opponent_collection_house_index = 13
    else:
        player_houses = houses_seed_count[7:13]  
        opponent_houses = houses_seed_count[0:6]  
        opponent_collection_house_index = 6

    if all(seeds == 0 for seeds in player_houses):
        houses_seed_count[opponent_collection_house_index] += sum(opponent_houses)

        for i in range(len(opponent_houses)):
            houses_seed_count[i] = 0

        display_houses = [" " + str(seed) if seed < 10 else str(seed) for seed in houses_seed_count]

        print("")
        print("-------------")
        print("----FINAL----")
        print("----BOARD----")
        print("-------------")
        print("")
        print("+----+----+----+----+----+----+----+----+")
        print(f"|    | {display_houses[12]} | {display_houses[11]} | {display_houses[10]} | {display_houses[9]} | {display_houses[8]} | {display_houses[7]} |    |")
        print(f"| {display_houses[13]} |----+----+----+----+----+----| {display_houses[6]} |")
        print(f"|    | {display_houses[0]} | {display_houses[1]} | {display_houses[2]} | {display_houses[3]} | {display_houses[4]} | {display_houses[5]} |    |")
        print("+----+----+----+----+----+----+----+----+")
        print("")
        print(f"Final Scores - Player One: {houses_seed_count[6]}, Player Two: {houses_seed_count[13]}")
        print("")

        if houses_seed_count[6] > houses_seed_count[13]:
            print("Player One wins!")
            print("")
        elif houses_seed_count[13] > houses_seed_count[6]:
            print("Player Two wins!")
            print("")
        else:
            print("It's a tie!")
            print("")
        break 

    if player_one:
        if message_code == 0:
            message = "Player One... you're up!"
        elif message_code == -1:
            message = "Invalid input. Have another go, Player One."
        elif message_code == -2:
            message = "You must choose a house with seeds, Player One. Try again."
    else:
        if message_code == 0:
            message = "Player Two... you're up!"
        elif message_code == -1:
            message = "Invalid input. Have another go, Player Two."
        elif message_code == -2:
            message = "You must choose a house with seeds, Player Two. Try again."
    print("")
    print(message)
    message_code = 0

    display_houses = [" " + str(seed) if seed < 10 else str(seed) for seed in houses_seed_count]

    print("")
    if not player_one:
        print("        a    b    c    d    e    f")
    print("+----+----+----+----+----+----+----+----+")
    print(f"|    | {display_houses[12]} | {display_houses[11]} | {display_houses[10]} | {display_houses[9]} | {display_houses[8]} | {display_houses[7]} |    |")
    print(f"| {display_houses[13]} |----+----+----+----+----+----| {display_houses[6]} |")
    print(f"|    | {display_houses[0]} | {display_houses[1]} | {display_houses[2]} | {display_houses[3]} | {display_houses[4]} | {display_houses[5]} |    |")
    print("+----+----+----+----+----+----+----+----+")
    if player_one:
        print("        f    e    d    c    b    a")
    print("")

    user_input = input("Enter a letter to choose the corresponding house or enter 'exit' to leave the game: ")

    selected_house = -1

    if user_input == "exit":
        playing = False
    else:
        if player_one:
            if user_input in "abcdef" and len(user_input) == 1:
                selected_house = "fedcba".index(user_input)
        else:
            if user_input in "abcdef" and len(user_input) == 1:
                selected_house = 7 + "fedcba".index(user_input)

        if selected_house == -1:
            message_code = -1
            continue

    seeds = 0

    if selected_house >= 0:
        seeds = houses_seed_count[selected_house]

    if seeds == 0:
        message_code = -2
        continue

    houses_seed_count[selected_house] = 0
        
    current_house = selected_house

    while seeds > 0:
        current_house += 1

        if current_house == 6:  
            current_house = 7
        elif current_house == 13:  
            current_house = 0

        houses_seed_count[current_house] = houses_seed_count[current_house] + 1
        seeds = seeds - 1

    captures = 0 

    check_house = current_house  

    while True:
        if player_one:
            if check_house in range(7, 13) and houses_seed_count[check_house] in [2, 3]:
                captures += houses_seed_count[check_house]
                houses_seed_count[check_house] = 0
                check_house -= 1
            else:
                break
        else:
            if check_house in range(0, 6) and houses_seed_count[check_house] in [2, 3]:
                captures += houses_seed_count[check_house]
                houses_seed_count[check_house] = 0
                check_house -= 1
            else:
                break

    if captures > 0:
        if player_one:
            houses_seed_count[6] = houses_seed_count[6] + captures
        else:
            houses_seed_count[13] = houses_seed_count[13] + captures

    player_one = not player_one