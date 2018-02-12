import random


def call_check(rand_num, number):
    if (number == rand_num):
        print("random guess by computer is", rand_num, "and it is exactly same")

    elif (number > rand_num):
        print("random guess by computer is", rand_num, "and it is too high")

    elif (number < rand_num):
        print("random guess by computer is", rand_num, "and it is too low")

    else:
        print("error")


def main():
    number = int(input(" enter a number between 1 and 9"))

    rand_num = random.choice(range(1, 10))

    call_check(rand_num, number)


main()
