#!/usr/bin/python3
import math
import player
import random


class card:
    def __init__(self, name, classification):
        self.name = name
        self.classification = classification
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = self.name + name
    def getClassification(self):
        return self.classification
    def setClassification(self, classification):
        self.classification = self.classification

#Function to create and set dictionary to hold cards
def setDeck():
    deck = {}
    for i in range (0, 52):
        #Set card values
        value = i % 13;
        if (value > 0 and value < 10):
            deck[i] = card(str(value+1), value+1)
        if (value == 0):
            deck[i] = card("Ace", 11)
        if (value == 10):
            deck[i] = card("Jack", 10)
        if (value == 11):
            deck[i] = card("Queen", 10)
        if (value == 12):
            deck[i] = card("King", 10)
        #Set card suits
        if (i > -1 and i < 13):
            deck[i].setName(" of Spades")
        if (i > 12 and i < 26):
            deck[i].setName(" of Hearts")
        if (i > 25 and i < 39):
            deck[i].setName(" of Clubs")
        if (i > 38 and i < 52):
            deck[i].setName(" of Diamonds")
    return deck

#Function to create and set cards_dealt vector
def setCardsDealt():
    cards_dealt = {}
    for i in range (0, 52):
        cards_dealt[i] = 0
    return cards_dealt

#Function to draw a random card
def draw(deck, cards_dealt):
    deck_index = random.randint(0,51)
    #check if random index is the same as one that's already in use
    if (cards_dealt[deck_index] == 0):
        cards_dealt[deck_index] = 1
        return deck[deck_index]
    return draw(deck, cards_dealt)

#Reset hands
def resetHands(Player):
    for i in range(2, len(Player.hand)):
        del(Player.hand[i])

def sortHand(hand_vec):
    #Simple sort for only 7 elements
    """This function sorts a hand based on classifications using simple sort.
    Args:
        hand_vec: a vector of 7 cards that represents the hand of a player.
    Returns:
        The same vector sorted by classification.
    """
    for i in range(0,7):
        for j in range(0,7):
            if (hand_vec[j].classification > hand_vec[i].classification):
                temp = hand_vec[i]
                hand_vec[i] = hand_vec[j]
                hand_vec[j] = temp
    return hand_vec

def aceHighOrLow(Player):
    ace_counter = 0
    optimal_total_with_11 = 0
    optimal_total_no_11 = 0
    for i in range(0, len(Player.hand)):
        if (Player.hand[i].getClassification() == 11 and ace_counter > 0):
            optimal_total_with_11 += 1
        elif (Player.hand[i].getClassification() == 11 and ace_counter == 0):
            optimal_total_with_11 += 11
            ace_counter = 1
            continue
        else:
            optimal_total_with_11 += Player.hand[i].getClassification()
    for i in range(0, len(Player.hand)):
        if (Player.hand[i].getClassification() == 11 and ace_counter > 0):
            optimal_total_no_11 += 1
        else:
            optimal_total_no_11 += Player.hand[i].getClassification()
    if (optimal_total_with_11 == 21):
        Player.setTotal(21)
    if (optimal_total_with_11 > 21):
        Player.setTotal(optimal_total_no_11)
    else:
        Player.setTotal(optimal_total_with_11)
