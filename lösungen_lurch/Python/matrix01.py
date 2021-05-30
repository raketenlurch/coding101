def print_matrix(number):
    for i in range(1, number+1):
        for j in range(1, number+1):
            print("#", end="")
        print()


user_input = int(input("Enter a number:"))
print_matrix(user_input)
