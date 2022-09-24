
MasterMind Projekt på H4
Et kode deducerings spil for en spiller.
Baseret på brætspillet Master Mind

Kør spillet enten gennem terminal der understøtter python eller gennem pycharm
*se pycharm_mode variable hvis du bruger terminal for et pænere output


#regler 
*Der blive brugt bogstaver i stedet for farver 
*Det er muligt at en farve dukke op 2 gange, men ikke mere end det.
    Spillet genere automatisk en løsning-kode du skal prøve at regne ud, du har x antal forsøg.
    Når du har inputtet et forslag til koden vil du få feedback i form af "P" og "C"
    "P" betyder korrekt placering og farve, "C" betyder forkert placering men rigtig farve
    Fx. "1xP 2xC" betyder at 1 farve er placeret korrekt og 2 har den rigtige farve men placeret forkert.
    Hvis farven ikke er med i løsningen, så bliver den ikke nævnt i tilbage meldingen

#følgende variabler kan ændres

*Vist med default værdier
    number_of_available_colors = 8    #kappet på 26 for at bruge hele alfabetet
    board_size = 4                    #kappet på 52  fordi hver farve kan bruges 2 gange
    number_of_turns = 8
    show_Answer = False               #sættes til true for at vise løsning på tur 1
    pycharm_mode = True               #sættes til false for et pænere output i terminaler på win,mac og linux ikke pycharm.

number_of_available_colors, board_size, number_of_turns kan justere sværhedsgraden af spillet
pycharm_mode ignore "clear" funktion på pycharm, da den ikke understøtter clear