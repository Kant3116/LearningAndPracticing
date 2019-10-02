for num in range(4, 21):
    if num % 4 == 0:
        print(num, ": divisible by 4 but it's also divisible by 2")
    elif num % 2 == 0:
        print(num, ": its also divisible by 2")
    else:
        print(num, "It's not divisible by 2")
