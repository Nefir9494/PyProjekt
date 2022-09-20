
#mod spiller = opret kode der skal gemmes med op til 2 kopier

#input af spillerens gæt

#afklar hvordan det matcher op mod koden

#Check om der er 2 af samme farve

#giv svar tilbage og vis tavlen med alle svar
import string
import random
number_of_available_colors = 8
board_size = 4
number_of_turns = 8
turn_nr = 0
alphabet = string.ascii_uppercase
colors = []
current_guess = []
opponents_list = []
players_previous_guesses = {}


#shortcut to make a random nr
def ran_nr():
    return random.randint(0, number_of_available_colors - 1)


def print_result(list_to_print):
    print("||{}||".format(".".join(list_to_print)))


def print_result1(list_to_print):
    print(f"||{*list_to_print,}||")


def checklist(test_value, testlist):
    if test_value not in testlist:
        #print("does not contains " + test_value)
        return True
    else:
        #print(" contains " + test_value)
        return False


#making the actual list of available colors
for i in range(number_of_available_colors):
    colors.append(alphabet[i])


def div():
    print("-" * 20)


def opponents_colors_to_guess():
    temp_1 = []
    temp_2 = []
    iter_to_unique = 0
    while iter_to_unique < board_size:
        value = (colors[ran_nr()])
        #print(value)
        if checklist(value, temp_1):
            temp_1.insert(iter_to_unique, value)
            opponents_list.append(value)
            iter_to_unique += 1
        elif checklist(value, temp_2):
            temp_2.insert(iter_to_unique, value)
            opponents_list.append(value)
            iter_to_unique += 1


def convert_input():
    clean_input = []
    while True:
        player_input = input("input:")
        if len(player_input) == board_size and player_input.isalpha():
            player_input = player_input.upper()
            clean_input[:0] = player_input
            return clean_input
        else:
            print("Wrong syntax for inputs")


def present_and_receive_input():
    div()
    print("Please enter your guess:\n use format \"ABCD\"\n Available colors:")
    print_result(colors)
    print_previous_guesses()

    guess = [convert_input()]

    return guess


def print_previous_guesses():
    for turn in range(turn_nr):
        pturn = ("turn" + str(turn))
        print_result(players_previous_guesses.values(pturn))


opponents_colors_to_guess()

while current_guess != opponents_list:

    div()
    print("opponents guess:")
    print_result(opponents_list)
    #create_previous_guess_dic()

    current_guess = present_and_receive_input()
    players_previous_guesses["turn" + str(turn_nr)] = current_guess
    print("currents guess")
    print_result(current_guess)
#print(colors)


