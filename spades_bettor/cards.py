#!/usr/bin/python3
import math
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
            deck[i] = card("Ace", 14)
        if (value == 10):
            deck[i] = card("Jack", 11)
        if (value == 11):
            deck[i] = card("Queen", 12)
        if (value == 12):
            deck[i] = card("King", 13)
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

def histogram(hand_vec):
    histogram = {}
    for i in range(0, 15):
        histogram[i] = 0

    for i in range(0, 7):
        histogram[hand_vec[i].getClassification()] += 1

    return histogram

def sortHand(suit_vec):
    #Simple sort for only 7 elements
    """This function sorts a hand based on classifications using simple sort.
    Args:
        suit_vec: a vector of cards that represents the cards of a certain
            suit that a user has
    Returns:
        The same vector sorted by classification.
    """
    for i in range(0, len(suit_vec)):
        for j in range(0, len(suit_vec)):
            if (suit_vec[j].classification > hand_vec[i].classification):
                temp = hand_vec[i]
                suit_vec[i] = hand_vec[j]
                suit_vec[j] = temp
