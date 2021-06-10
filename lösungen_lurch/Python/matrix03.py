import random

# Lösung mit Kommentaren
"""def print_matrix_random_characters(width, height, random_character):
    digits_of_rectangle = width * height
    random_digits = []

    # jeder Zahl aus random_characters einen zufälligen Wert zuweisen
    # for i in range(random_characters): (https://www.python.org/dev/peps/pep-0204/)
    #for i in range(1, random_character+1):
    while len(random_digits) <= random_character-1:
        random_position = random.randint(0, digits_of_rectangle)
        #random_digits.append(random_position)

        if random_position in random_digits:
            #print("Before", random_digits)
            random_digits.remove(random_position)
            #random_character -= 1
            #print("After", random_digits)

        random_digits.append(random_position)

    #print(random_digits)
    for i in range(1, digits_of_rectangle+1):
        if i in random_digits:
            print("*", end="")
        else:
            print("#", end="")

        if i % width == 0:
            print()

# user input
width = int(input("Width:"))
height = int(input("Height:"))
randoms = int(input("Randoms:"))

print_matrix_random_characters(width, height, randoms)
"""
# Lösung ohne Kommentare


def print_matrix_random_characters(width, height, random_character):
    digits_of_rectangle = width * height
    random_digits = []

    while len(random_digits) < random_character:
        random_position = random.randrange(0, digits_of_rectangle)

        if random_position in random_digits:
            random_digits.remove(random_position)

        random_digits.append(random_position)

    for i in range(0, digits_of_rectangle):
        if i in random_digits:
            print("*", end="")
        else:
            print("#", end="")

        # Lässt sich mathematisch bestimmt noch schöner lösen
        if (i+1) % width == 0:
            print()


# user input
width = int(input("Width:"))
height = int(input("Height:"))
randoms = int(input("Randoms:"))

print_matrix_random_characters(width, height, randoms)
