
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
previous_guesses_dic = {}



#shortcut to make a random nr
def ran_nr():
    return random.randint(0, number_of_available_colors - 1)


def print_result(list_to_print):
    print("||{}||".format(".".join(list_to_print)))


def checklist(test_value, testlist):
    if test_value not in testlist:
        return True
    else:
        return False


def div():
    print("-" * 20)


def opponents_colors_to_guess():
    temp_1 = []
    temp_2 = []
    iter_to_unique = 0
    while iter_to_unique < board_size:
        value = (colors[ran_nr()])
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
            round_turn = "turn" + str(turn_nr)
            previous_guesses_dic[round_turn] = player_input
            clean_input[:0] = player_input
            return clean_input
        else:
            print("Wrong syntax for inputs")


def present_and_receive_input():
    div()
    print("Please enter your guess:\n use format \"ABCD\"\n Available colors:")
    print_result(colors)
    for turn in previous_guesses_dic.values():
        print_result(turn)
    div()
    guess = [convert_input()]
    return guess


#making the actual list of available colors
for i in range(number_of_available_colors):
    colors.append(alphabet[i])
opponents_colors_to_guess()

#debug for at checke om gæt er korrekt
div()
print("opponents guess:")
print_result(opponents_list)
div()


while current_guess != opponents_list:
    current_guess = present_and_receive_input()
    turn_nr += 1



