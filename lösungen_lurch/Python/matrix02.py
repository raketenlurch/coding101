import random

def print_matrix_random_character(number):
    digits_of_square = number * number
    random_number = random.randrange(1, digits_of_square)

    for i in range(1, digits_of_square+1):
        if i == random_number:
            print("*", end="")
        else:
            print("#", end="")

        if i % number == 0:
            print()


user_input = int(input("Enter a number:"))
print_matrix_random_character(user_input)
