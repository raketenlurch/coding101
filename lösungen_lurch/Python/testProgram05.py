text = input("Text:")
filename = input("Dateiname:")

with open(filename, "w") as file:
    file.write(text)
