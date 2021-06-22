with open("numbers.txt", "w") as number:
    for i in range(1, 100):
        if i % 5 == 0:
            number.write(str(i) + "\n")
