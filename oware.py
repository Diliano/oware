houses_seed_count = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

playing = True

while playing:

    print("+----+----+----+----+----+----+----+----+")
    print("|    |    |    |    |    |    |    |    |")
    print("|    |----+----+----+----+----+----|    |")
    print("|    |    |    |    |    |    |    |    |")
    print("+----+----+----+----+----+----+----+----+")
    print("")

    user_input = input("Enter 'exit' to leave the game: ")

    if user_input == "exit":
        playing = False