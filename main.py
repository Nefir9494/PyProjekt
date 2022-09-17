
#mod spiller = opret kode der skal gemmes med op til 2 kopier

#input af spillerens gæt

#afklar hvordan det matcher op mod koden

#Check om der er 2 af samme farve

#giv svar tilbage og vis tavlen med alle svar
import string
import random
number_of_available_colors = 8 - 1
board_size = 4
alphabet = string.ascii_uppercase
colors = []
guess_list = []


#shortcut to make a random nr
def nr():
    return random.randint(0, number_of_available_colors)


def print_result(list_to_print):
    print("||{}||".format(".".join(list_to_print)))


for i in range(number_of_available_colors + 1):
    colors.append(alphabet[i])


print(colors)


for i in range(board_size):
    value = (colors[nr()])
    guess_list.append(value)





print_result(guess_list)

