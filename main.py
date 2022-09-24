import string
import random
from os import system, name
# Customise difficulty variables and user modes
# -----------------------
number_of_available_colors = 26
board_size = 52
number_of_turns = 99999999
show_Answer = False
pycharm_mode = True
# -----------------------

# Variables used throughout the game
turn_nr = 0
alphabet = string.ascii_uppercase
colors = []
current_guess = []
opponents_list = []
previous_guesses_dic = {}
spacer = "      "
game_state = True


# Lav en liste til printbar string
def print_result(list_to_print):
    return "||{}||".format(".".join(list_to_print))


# Check om værdi ikke er i en liste
def checklist(test_value, testlist):
    if test_value not in testlist:
        return True
    else:
        return False


# Pynt til lave et passende antal bindestreger
def div():
    print(spacer + "-" * ((board_size * 2) + 12))


# Clear Konsol - virker ikke i pycharm kaster error - kan skifte variable pycharm_mode for at fjerne fejl
def clear():
    if pycharm_mode:
        return
    elif name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# Oprettelse af farvekombiantion som skal gættes- det er kun tilladt at der er op til 2 unique
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


# Retter bruger input til korrekt format
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


# Præsentere spilbrættet
def present_input():
    div()
    print("Please enter your guess:\n Use format \"ABCD\"\n Available colors:")
    print(("Turn: " + str(turn_nr) + " ") + print_result(colors))
    if turn_nr != 0:
        div()
    for turn in previous_guesses_dic.values():
        print(spacer + turn)
    div()


# Check på hvor korrekt spillerens svar er
def feedback_guess():
    pos = xpos1 = xpos2 = 0
    feedback = []
    new_guess = current_guess.copy()
    solution = opponents_list.copy()
    # Fylder liste med korrekt antal "tomme" felter
    for x in range(board_size):
        feedback.append("none")
    # Checker efter korrekt placering og farve og markere med "P"
    while pos < board_size:
        if new_guess[pos] == solution[pos]:
            feedback[pos] = "P"
            new_guess[pos] = solution[pos] = "none"
        pos += 1
    # Checker efter forkert placering og korrekt farve og markere med "C"
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
    # Feedback - hvor det kun er antal af "P" og "C" og ikke placring der bliver udleveret
    con_feedback = "%sxP %sxC" % ((feedback.count("P")), (feedback.count("C")))
    return con_feedback


# Check om spillet skal forsætte
def check_victory(wincon):
    if wincon == opponents_list:
        return "Won"
    if turn_nr == number_of_turns:
        return "Lost"
    else:
        return True


# Start på spillet
clear()
# Making the actual list of available colors
for letter in range(number_of_available_colors):
    colors.append(alphabet[letter])
opponents_colors_to_guess()


# Debug for at checke om gæt er korrekt
if show_Answer:
    div()
    print("Opponents guess:")
    print(print_result(opponents_list))
    div()

print("Welcome to MasterMind")
print("You have " + str(number_of_turns) + " tries")

# Primært gameloop
# True er specificeret for at kunne acceptere andre gamestates
while game_state == True:
    present_input()
    current_guess = convert_input()
    feed = feedback_guess()
    # Sætter feedback sammen med den eksisterende data i dictionary
    previous_guesses_dic["turn" + str(turn_nr)] = str(previous_guesses_dic["turn" + str(turn_nr)] + feed + "||")
    turn_nr += 1
    game_state = check_victory(current_guess)
    clear()

# Afslutning på spillet og afsløring af resultat hvis det er tabt
div()
div()
print(spacer + "You %s!!" % game_state)
if game_state == "Lost":
    print(spacer + "Try again")
    print("Correct Solution:\n" + spacer + print_result(opponents_list))
print("Previous Guess")
for turn in previous_guesses_dic.values():
    print(spacer + turn)
div()


