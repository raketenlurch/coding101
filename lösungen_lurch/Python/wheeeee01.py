def duplicateHashtag(amount):
    hashtags = ''

    for i in range(0, amount):
        hashtags += "#"

    return hashtags

# user input
number = int(input("Enter MAX:"))

for i in range(1, number+1):
    print(duplicateHashtag(i))
