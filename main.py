
#mod spiller = opret kode der skal gemmes med op til 2 kopier

#input af spillerens gæt

#afklar hvordan det matcher op mod koden

#Check om der er 2 af samme farve

#giv svar tilbage og vis tavlen med alle svar
import string
import random
from os import system, name
#Customise difficulty variables
#-----------------------
number_of_available_colors = 8
board_size = 4
number_of_turns = 3
Show_Answer = False
#-----------------------

#Variables used throughout the game
turn_nr = 0
alphabet = string.ascii_uppercase
colors = []
current_guess = []
opponents_list = []
previous_guesses_dic = {}
spacer = "      "
game_state = True


#Lav en liste til printbar string
def print_result(list_to_print):
    return "||{}||".format(".".join(list_to_print))


#check om værdi ikke er i en liste
def checklist(test_value, testlist):
    if test_value not in testlist:
        return True
    else:
        return False


#Pynt til lave et passende antal bindestreger
def div():
    print(spacer + "-" * ((board_size * 2) + 12))


#clearer consollen - virker ikke i pycharm
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


#Oprettelse af farvekombiantion som skal gættes- det er kun tilladt at der er op til 2 unique
def opponents_colors_to_guess():
    temp_1 = []
    temp_2 = []
    iter_to_unique = 0
    while iter_to_unique < board_size:
        value = (colors[random.randint(0, number_of_available_colors - 1)])
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
            previous_guesses_dic[round_turn] = print_result(player_input)
            clean_input[:0] = player_input
            return clean_input
        else:
            print("Wrong syntax for inputs")


def present_input():
    div()
    print("Please enter your guess:\n Use format \"ABCD\"\n Available colors:")
    print(("Turn: " + str(turn_nr) + " ") + print_result(colors))
    if turn_nr != 0:
        div()
    for turn in previous_guesses_dic.values():
        print(spacer + turn)
    div()
    #guess = convert_input()
   # return guess


def feedback_guess():
    pos = xpos1 = xpos2 = 0
    feedback = []
    new_guess = current_guess.copy()
    solution = opponents_list.copy()
    for x in range(board_size):
        feedback.append("none")
    #print(print_result(feedback))
    while pos < board_size:
        if new_guess[pos] == solution[pos]:
            feedback[pos] = "P"
            new_guess[pos] = solution[pos] = "none"
        pos += 1
    while xpos1 < len(new_guess):
        while xpos2 < len(solution):
            if new_guess[xpos1] == solution[xpos2] and (new_guess[xpos1] != "none"):
                feedback[xpos1] = "C"
                new_guess[xpos1] = solution[xpos2] = "none"
                xpos2 = len(solution)
            else:
                xpos2 += 1
        xpos2 = 0
        xpos1 += 1
    con_feedback = "%sxP %sxC"%((feedback.count("P")), (feedback.count("C")))
    return con_feedback


def check_victory(wincon):
    if wincon == opponents_list:
        return "Won"
    if turn_nr == number_of_turns:
        return "Lost"
    else:
        return True


clear()
#making the actual list of available colors
for letter in range(number_of_available_colors):
    colors.append(alphabet[letter])
opponents_colors_to_guess()


#debug for at checke om gæt er korrekt
if Show_Answer:
    div()
    print("Opponents guess:")
    print(print_result(opponents_list))
    div()

print("Welcome to MasterMind")
print("You have " + str(number_of_turns) + " tries")
#True er specificeret for at kunne acceptere andre gamestates
while game_state == True:

    present_input()
    current_guess = convert_input()
    feed = feedback_guess()
    #print(feed)

    previous_guesses_dic["turn" + str(turn_nr)] = str(previous_guesses_dic["turn" + str(turn_nr)] + feed + "||")
        #print(feedback_guess())
    #print(current_guess)
    turn_nr += 1
    game_state = check_victory(current_guess)
    clear()
    #print(game_state)

div()
div()
print(spacer + "You %s!!"%game_state)
if game_state == "Lost":
    print(spacer + "Try again")
    print("Correct Solution:\n" + spacer + print_result(opponents_list))
print("Previous Guess")
for turn in previous_guesses_dic.values():
    print(spacer + turn)
div()


