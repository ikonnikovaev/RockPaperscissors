import random


help_string = "Rock-Paper-Scissors"


def read_rating(filename):
    rating_dict = {}
    f = open(filename)
    for line in f:
        name, rating = line.split()
        rating = int(rating)
        rating_dict[name] = rating
    f.close()
    return rating_dict


def check_result(user_option, computer_option, options):
    if user_option == computer_option:
        return 0

    n_options = len(options)
    n_winning = n_options // 2

    for i in range(0, n_options):
        if (options[i] == user_option):
            for j in range(0, n_winning):
                if (options[(i + j + 1) % n_options] == computer_option):
                    return -1
            break

    return 1


def print_result(user_option, computer_option, options):
    res = check_result(user_option, computer_option, options)
    if res == 0:
        print("There is a draw ({})".format(user_option))
    elif res == 1:
        print("Well done. Computer chose {} and failed".format(computer_option))
    elif res == -1:
        print("Sorry, but computer chose {}".format(computer_option))
    return res



default_options = ["rock", "paper", "scissors"]
user_name = input("Enter your name: ")
print("Hello, {}".format(user_name))

rating = read_rating("rating.txt")
if user_name not in rating:
    rating[user_name] = 0


options = default_options
options_set = False

while (True):
    user_input = input()
    if not options_set:
        options_set = True

        if len(user_input.split(',')) >= 3:
            options = user_input.split(',')
        if len(user_input) == 0:
            pass
        print("Okay, let's start")
        continue



    if user_input == "!exit":
        print("Bye!")
        break
    elif user_input == "!rating":
        print("Your rating: {}".format(rating[user_name]))
    elif user_input == "!help":
        print(help_string)
    else:
        user_option = user_input
        computer_option = random.choice(options)
        res = print_result(user_option, computer_option, options)
        rating[user_name] += (res + 1) * 50




