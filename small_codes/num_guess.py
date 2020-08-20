from random import SystemRandom


def guess_num_check(num: int):

    if num % 2 == 0:
        print("Its a even number")
    elif num % 2 != 0:
        print("Its a odd number")


# score = 10
def score_keep(score: int):
    score -= 1
    print(score)


if __name__ == "__main__":
    random_gen = SystemRandom()
    X = random_gen.randrange(100)
    hint = input("Hint needed? (Y or N) :  ",)
    hint = hint.lower()
    # score = 10
    if hint == "y":
        score_keep(10)
