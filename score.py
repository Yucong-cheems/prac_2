import random


def main():

    score = float(input("Enter score: "))
    print_score(score)
    generate_ramdom_score()


def print_score(score):
    if score > 100 or score < 0:
        print("Invalid score")
    if score > 50:
        print("Passable")
    if score > 90:
        print("Excellent")
    if score < 50:
        print("Bad")
    return score

def generate_ramdom_score():
    score = random.randint(0, 100)
    print("result: ", score)
    return score

main()