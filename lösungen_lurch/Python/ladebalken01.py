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
load = int(input("Enter a state:"))
if load >= 1 and load <= 10:
    print_loading_bar(load)
else:
    print("The number is too big or too low.")
