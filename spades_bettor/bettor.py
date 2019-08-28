#!/usr/bin/python3
import math
import random
import cards

def main():
    #print("Directions and how to use this program")
    hand = {}
    for i in range(0, 13):
        if (i == 0):
            hand[i] = input("Please enter first card: ")
        elif (i > 0 and i < 12):
            hand[i] = input("Please enter next card: ")
        else:
            hand[i] = input("Please enter last card: ")
    #sort hand by rank and by suit
    #Check for aces, kings, queens, jacks
    #Check for spades versus holes in suits
    #Check for high spades
    #return safe bet, optimal bet, risky bet (not necessarily different)
main()

