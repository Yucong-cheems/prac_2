
MENU = """ G - Get a valid score
 P - Print result
 S - how stars
 Q - uit"""


def main():

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_score()
            print(score)
        elif choice == "P":
            print(print_score(score))
        elif choice == "S":
            print_star(score)
        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>> ").upper()
    print("Bye")


def get_score():
    input_score = float(input("Enter score: "))
    while input_score < 0 or input_score > 100:
        print("Invalid score!")
        input_score = float(input("Enter score: "))
    return int(input_score)


def print_score(score):
    if score > 100 or score < 0:
        print("Invalid score")
    if score > 50:
        print("Passable")
    if score > 90:
        print("Excellent")
    if score < 50:
        print("Bad")


def print_star(score):
    print(score * '*')
    print("Bye")


main()