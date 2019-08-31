#!/usr/bin/python3
import math
import random
import cards

#Global dicts so we don't have to pass all of them to suitSort
#Separate hand by suit, sort by rank after input


#Could have used Python's Merge function here, but I thought this would
#be a good exercise
def combineVectors(vec0, vec1, vec2, vec3):

    sorted_hand = {}
    #For scalability you can add vec lengths
    #For our purposes this number should always be 13
    hand_length = len(vec0) + len(vec1) + len(vec2) + len(vec3)
    vec0_index = 0
    vec1_index = len(vec0)
    vec2_index = len(vec0)+ len(vec1)
    vec3_index = len(vec0)+ len(vec1) + len(vec2)
    for i in range(0, hand_length):
        if (i < vec1_index):
            sorted_hand[i] = vec0[vec0_index]
            vec0_index += 1
        if (i < vec2_index):
            sorted_hand[i] = vec1[vec1_index]
            vec1_index += 1
        if (i < vec3_index):
            sorted_hand[i] = vec2[vec2_index]
            vec2_index += 1
        else:
            sorted_hand[i] = vec3[vec3_index]
            vec3_index += 1

    return sorted_hand


def main():
    spades = {}
    hearts = {}
    clubs = {}
    diamonds = {}
    spades_index = 0
    hearts_index = 0
    clubs_index = 0
    diamonds_index = 0
    #print("Directions and how to use this program")
    #May not need this dict later, but we'll see
    hand = {}

    #Declare best hand

    #Input hand
    for i in range(0, 13):
        if (i == 0):
            hand[i] = input("Please enter first card: ")

        elif (i > 0 and i < 12):
            hand[i] = input("Please enter next card: ")

        else:
            hand[i] = input("Please enter last card: ")

        str = hand[i]
        if (str[-1:] == "S"):
            spades[spades_index] = str
            spades_index += 1
        if (str[-1:] == "H"):
            hearts[hearts_index] = str
            hearts_index += 1
        if (str[-1:] == "C"):
            clubs[clubs_index] = str
            clubs_index += 1
        if (str[-1:] == "D"):
            diamonds[diamonds_index] = str
            diamonds_index += 1

    cards.suitSort(spades)
    cards.suitSort(hearts)
    cards.suitSort(clubs)
    cards.suitSort(diamonds)

    sortedHand = combineVectors(spades, hearts, clubs, diamonds)

    for i in sortedHand:
        print(sortedHand[i])
    #sort hand by rank and by suit
    #Check for aces, kings, queens
    #Check for spades versus holes in suits
    #Check for high spades
    #return safe bet, optimal bet, risky bet (not necessarily different)
main()
