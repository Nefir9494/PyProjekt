
#mod spiller = opret kode der skal gemmes med op til 2 kopier

#input af spillerens gæt

#afklar hvordan det matcher op mod koden

#Check om der er 2 af samme farve

#giv svar tilbage og vis tavlen med alle svar

import random
random.seed(2)


for _ in range(4):
    value = (random.randint(0,10))
    print(value)

