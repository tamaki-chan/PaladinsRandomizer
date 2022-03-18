# File: PaladongsRamdomizer.py
# Picks a random champion and load out for you to use in a match.... sorta
# Created By: QueenMomiji

import random

def main():

    input ("Press Enter to start")

    contents = []

    with open('Champions.txt') as rnd:
        for line in rnd:
            line=line.strip()
            contents.append(line)

    print ("Random champion:", contents[random.randint(0,len(contents)-1)])

    talent = random.randint(1,3)
    
    print ("Your talent is:", talent)

    card_1 = random.randint(1,16)
    
    card_2 = random.randint(1,16)
    
    while True:
        if card_1 == card_2:
            card_2 = random.randint(1_16)
        else:
            break
    card_3 = random.randint(1,16)
    
    while True:
        if card_2 == card_3:
            card_3 = random.randint(1_16)
        else:
            break
    card_4 = random.randint(1,16)
    
    while True:
        if card_3 == card_4:
            card_4 = random.randint(1_16)
        else:
            break
    card_5 = random.randint(1,16)
    
    while True:
        if card_4 == card_5:
            card_5 = random.randint(1_16)
        else:
            break

    print ("Your cards are:", card_1, card_2, card_3, card_4, card_5)

    level_1 = random.randint(1,5)
    level_2 = random.randint(1,5)
    level_3 = random.randint(1,5)
    level_4 = random.randint(1,5)
    level_5 = random.randint(1,5)
    
    while True:
        if level_1 + level_2 + level_3 + level_4 + level_5 > 15 or level_1 + level_2 + level_3 + level_4 + level_5 < 15:
            level_1 = random.randint(1,5)
            level_2 = random.randint(1,5)
            level_3 = random.randint(1,5)
            level_4 = random.randint(1,5)
            level_5 = random.randint(1,5)
        else:
            break
        
    print("Your card levels are:", level_1, level_2, level_3, level_4, level_5)
    
main()
