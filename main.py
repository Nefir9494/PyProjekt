
#mod spiller = opret kode der skal gemmes med op til 2 kopier

#input af spillerens gæt

#afklar hvordan det matcher op mod koden

#Check om der er 2 af samme farve

#giv svar tilbage og vis tavlen med alle svar
import string
import random
number_of_available_colors = 8
board_size = 4
alphabet = string.ascii_uppercase
colors = []
guess_list = []



#shortcut to make a random nr
def ran_nr():
    return random.randint(0, number_of_available_colors - 1)


def print_result(list_to_print):
    print("||{}||".format(".".join(list_to_print)))


def checklist(test_value, testlist):
    if test_value not in testlist:
        print("does not contains " + test_value)
        return True
    else:
        print(" contains " + test_value)
        return False


#making the actual list of available colors
for i in range(number_of_available_colors):
    colors.append(alphabet[i])


def opponents_colors_to_guess():
    temp_1 = []
    temp_2 = []
    iter_to_unique = 0
    while iter_to_unique < board_size:
        value = (colors[ran_nr()])
        print(value)
        if checklist(value, temp_1):
            temp_1.insert(iter_to_unique, value)
            guess_list.append(value)
            iter_to_unique += 1
        elif checklist(value, temp_2):
            temp_2.insert(iter_to_unique, value)
            guess_list.append(value)
            iter_to_unique += 1


def present_input():
    print("Please enter your guess:\n use format \"ABCD\"\n Available colors:")
    print_result(colors)
    input1 = input("input:")
    return input1


opponents_colors_to_guess()
print(present_input())
print(colors)
print_result(guess_list)

