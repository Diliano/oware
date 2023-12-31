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