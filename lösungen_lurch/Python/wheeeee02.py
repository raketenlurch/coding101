def duplicate_hashtag(amount):
    hashtags = ''

    for i in range(0, amount):
        hashtags += "#"

    return hashtags


# user input
number = int(input("Enter MAX:"))

for i in range(1, number+1):
    print(duplicate_hashtag(i))

for i in range(number-1, 0, -1):
    print(duplicate_hashtag(i))
