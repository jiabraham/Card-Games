#!/usr/bin/python3
import math
import random
import player

class Player:
    def __init__(self, money, name, status):
        self.money = money
        self.hand = {}
        self.name = name
        self.status = 0

#Function to create and set dictionary to hold cards
def setDeck():
    deck = {}
    for i in range (0, 52):
        #Set card values
        value = i % 13;
        if (value > 0 and value < 10):
            deck[i] = str(value+1)
        if (value == 0):
            deck[i] = "Ace"
        if (value == 10):
            deck[i] = "Jack"
        if (value == 11):
            deck[i] = "Queen"
        if (value == 12):
            deck[i] = "King"
        #Set card suits
        if (i > -1 and i < 13):
            deck[i]+= " of Spades"
        if (i > 12 and i < 26):
            deck[i]+= " of Hearts"
        if (i > 25 and i < 39):
            deck[i]+= " of Clubs"
        if (i > 38 and i < 52):
            deck[i]+= " of Diamonds"
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

#Function to set the flop
def dealFlop(deck, cards_dealt):
    pool = {}
    pool[0] = draw(deck, cards_dealt)
    pool[1] = draw(deck, cards_dealt)
    pool[2] = draw(deck, cards_dealt)
    return pool

#Function to deal the turn card
def dealTurn(deck, cards_dealt, pool):
    pool[3] = draw(deck, cards_dealt)
    return pool

#Function to deal the river card
def dealRiver(deck, cards_deal, pool):
    pool[4] = draw(deck, cards_dealt)
    return pool

#UNFINISHED
#Function to rank who has the best hand at the end of a round
#Make scalable later, for now 4 players
def handRanking(player_vector, pool):
    player_vector_index = 0
    hand_rankings = {}
    while (player_vector_index < player_vector.size()):
        #If the player has reached the end of the final betting phase
        if (player_vector[player_vector_index].getStatus() == 1):
            hand_vec = player_vector[player_vector_index].getHand()
            hand_vec[2] = pool[0]
            hand_vec[3] = pool[1]
            hand_vec[4] = pool[2]
            hand_vec[5] = pool[3]
            hand_vec[6] = pool[4]
            handRankings[player_vector_index] = classifyHand(hand_vec)


        player_vector_index = player_vector_index + 1
            return "winning hand is"
#UNFINISHED
#Function to return a hand ranking 1-10
#May have to edit later to include high card to differentiate same ranking
def classifyHand(hand_vec):
    #First we should sort the hand based on values(bubble-sort of 7 elements is negligible)
    k = 0
    hand_vec_length = len(hand_vec)
    flush_count = {}
    flush_count["spades"] = 0
    flush_count["hearts"] = 0
    flush_count["clubs"] = 0
    flush_count["diamonds"] = 0
    flush = False
    while (k < hand_vec_length):
        if (hand_vec[k][-6:] == "Spades"):
            flush_count["spades"] = flush_count["spades"] + 1
            if (flush_count["spades"] > 4):
                flush  = True
        if (hand_vec[k][-6:] == "Hearts"):
            flush_count["hearts"] = flush_count["hearts"] + 1
            if (flush_count["hearts"] > 4):
                flush  = True
        if (hand_vec[k][-5:] == "Clubs"):
            flush_count["clubs"] = flush_count["clubs"] + 1
            if (flush_count["clubs"] > 4):
                flush  = True
        if (hand_vec[k][-8:] == "Diamonds"):
            flush_count["diamonds"] = flush_count["diamonds"] + 1
            if (flush_count["diamonds"] > 4):
                flush  = True

def sortHand(hand_vec):
    for i in range(0,7):
        for j in range(1,7):
            if ((hand_vec[i][:3]) == "Ace")
