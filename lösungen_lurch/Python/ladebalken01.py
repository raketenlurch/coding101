def print_loading_bar(percentage):
    full_loading_bar = 10

    print("[", end="")

    for i in range(1, percentage+1):
        print("#", end="")

    for i in range(percentage, full_loading_bar):
        print(" ", end="")

    print("]", end="")

    print(" " + str(percentage) + "0 %",  end="")
    print()


# user input
load = int(input("Please enter a percentage:"))
print_loading_bar(load)
