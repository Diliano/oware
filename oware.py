houses_seed_count = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

playing = True

while playing:

    for i in range(0, len(houses_seed_count)):
        houses_seed_count[i] = int(houses_seed_count[i])
        if houses_seed_count[i] < 10:
            houses_seed_count[i] = " " + str(houses_seed_count[i])

    print("+----+----+----+----+----+----+----+----+")
    print("|    |    |    |    |    |    |    |    |")
    print("|    |----+----+----+----+----+----|    |")
    print("|    |    |    |    |    |    |    |    |")
    print("+----+----+----+----+----+----+----+----+")
    print("")

    user_input = input("Enter 'exit' to leave the game: ")

    if user_input == "exit":
        playing = False