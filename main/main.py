from random import randint


def random_num(min, max):
    num = randint(min, max)
    return num


def main():
    num = random_num(1,10)
    print(num)
    if num == 10:
        print("win")
    else:
        print("try again")


if __name__ == '__main__':
    main()
