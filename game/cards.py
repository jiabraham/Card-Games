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
    burn = {}
    burn[0] = draw(deck, cards_dealt)
    pool[0] = draw(deck, cards_dealt)
    pool[1] = draw(deck, cards_dealt)
    pool[2] = draw(deck, cards_dealt)
    return pool

#Function to deal the turn card
def dealTurn(deck, cards_dealt, pool, burn):
    burn[1] = draw(deck, cards_dealt)
    pool[3] = draw(deck, cards_dealt)
    return pool

#Function to deal the river card
def dealRiver(deck, cards_deal, pool, burn):
    burn[2] = draw(deck, cards_dealt)
    pool[4] = draw(deck, cards_dealt)
    return pool

#DONE
def sortHand(hand_vec):
    #Simple sort for only 7 elements
    for i in range(0,7):
        for j in range(0,7):
            if (hand_vec[j].classification > hand_vec[i].classification):
                temp = hand_vec[i]
                hand_vec[i] = hand_vec[j]
                hand_vec[j] = temp
    return hand_vec

def convertToMultiple(num):
    if (len(str(num)) != 2):
        num = "0" + str(num)
    else:
        num = str(num)
    return num

def padRanking(ranking):
    if (len(ranking) != 5):
        for i in range (0, 5-len(ranking)):
            ranking += "0"
    return ranking

def flush(hand_vec):
    best_score = "0";

    spades_vec = {}
    spades_vec_counter = 0
    hearts_vec = {}
    hearts_vec_counter = 0
    clubs_vec = {}
    clubs_vec_counter = 0
    diamonds_vec = {}
    diamonds_vec_counter = 0


    #Loop once through hand to count the number of each suit
    for k in range(0, 7):
        if (hand_vec[k].getName()[-6:] == "Spades"):
            spades_vec[spades_vec_counter] = hand_vec[k]
            spades_vec_counter += 1
            if (spades_vec_counter > 4):
                straight_flush = straight(spades_vec)
                if (straight_flush):
                    print("straight flush found spades = " + straight_flush)
                    best_score = "9" + straight_flush[1:3]
                else:
                    best_score = "6" + str(hand_vec[k].getClassification())
                flush  = True

        if (hand_vec[k].getName()[-6:] == "Hearts"):
            hearts_vec[hearts_vec_counter] = hand_vec[k]
            hearts_vec_counter += 1
            if (hearts_vec_counter > 4):
                straight_flush = straight(hearts_vec)
                if (straight_flush):
                    print("straight flush found hearts = " + straight_flush)
                    best_score = "9" + straight_flush[1:3]
                else:
                    best_score = "6" + str(hand_vec[k].getClassification())
                flush  = True

        if (hand_vec[k].getName()[-5:] == "Clubs"):
            clubs_vec[clubs_vec_counter] = hand_vec[k]
            clubs_vec_counter += 1
            if (clubs_vec_counter > 4):
                straight_flush = straight(clubs_vec)
                if (straight_flush):
                    print("straight flush found clubs = " + straight_flush)
                    best_score = "9" + straight_flush[1:3]
                else:
                    best_score = "6" + str(hand_vec[k].getClassification())
                flush  = True

        if (hand_vec[k].getName()[-8:] == "Diamonds"):
            diamonds_vec[diamonds_vec_counter] = hand_vec[k]
            diamonds_vec_counter += 1
            if (diamonds_vec_counter > 4):
                straight_flush = straight(diamonds_vec)
                if (straight_flush == "0"):
                    best_score = "6" + str(hand_vec[k].getClassification())
                    print("best_score_flush = " + best_score)
                else:
                    print("straight flush found diamonds = " + straight_flush)
                    best_score = "9" + straight_flush[1:3]
                    print("best_score_diamonds = " + best_score)
                flush  = True
    return best_score

def straight(hand_vec):

    #Declare counter and best_score
    straight_counter = 1
    best_score = "0"

    for i in range(0, len(hand_vec)-1):
        if (hand_vec[i].getClassification() == hand_vec[i+1].getClassification()):
            continue
        if (hand_vec[i].getClassification() + 1 == hand_vec[i+1].getClassification()):
            straight_counter += 1
        else:
            straight_counter = 1
        if (straight_counter == 4 and hand_vec[i].getClassification() == 4):
            if (hand_vec[4].getClassification() == 14 or hand_vec[5].getClassification() == 14 or hand_vec[6].getClassification() == 14):
                best_score = "505"
        if (straight_counter > 4):
            best_score = "5" + convertToMultiple(hand_vec[i+1].getClassification())
    return best_score

def multiple(hand_vec):

    #Declare best score variable
    #May want to make this an object to keep a string representation
    best_score = "0"

    #booleans for different types of multiples (may not need all of these)
    pair = False
    two_pair = False
    triplets = False
    full_house = False
    quadruples = False


    #Declare hand histogram vector and set initial values(with padding)
    histogram = {}
    for i in range(0, 15):
        histogram[i] = 0

    for i in range(0, 7):
        histogram[hand_vec[i].getClassification()] += 1

    #return histogram
    #Need to consider every possible outcome for frequencies (1-4)
    for i in range(0, 15):
        if (histogram[i] == 0):
            continue
        if (histogram[i] == 2):
            if (quadruples):
                continue
            if (full_house):
                best_score = "7" + best_score[3:]
            if (triplets):
                best_score = "7" + convertToMultiple(i) + best_score[1:]
                full_house = True
                continue
            if (two_pair):
                best_score = "3" + best_score[3:5] + convertToMultiple(i)
                continue
            if (pair):
                best_score = "3" + best_score[1:3] + convertToMultiple(i)
                two_pair = True
                continue
            best_score = "2" + convertToMultiple(i)
            pair = True
        if (histogram[i] == 3):
            if (quadruples):
                continue
            if (two_pair):
                best_score = "7" + best_score[3:5] + convertToMultiple(i)
                full_house = True
                continue
            if (pair):
                best_score = "7" + convertToMultiple(i) + best_score[1:]
                full_house = True
                continue
            if (triplets):
                best_score = "4" + convertToMultiple(i)
                triplets = True
                continue
            else:
                best_score = "4" + convertToMultiple(i)
                triplets = True
                continue
        if (histogram[i] == 4):
            best_score = "8" + convertToMultiple(i)
            quadruples = True
    if (best_score == ""):
        best_score = "1" + str(hand_vec[6].getClassification())
    return best_score

#Function to return a hand ranking 1-10
#May have to edit later to include high card to differentiate same ranking
def classifyHand(hand_vec):
    best_score = 0
    hand_vec = sortHand(hand_vec)

    #Need to return actual vectors to check for straight flush
    best_score_multiple = multiple(hand_vec)
    best_score_straight = straight(hand_vec)
    best_score_flush = flush(hand_vec)

    print("best_multiple = " + best_score_multiple)
    print("best_score_straight = " + best_score_straight)
    print("best_score_flush = " + best_score_flush)

    #Need to put checks in place for royal flush
    if (int(best_score_multiple[0:1]) > int(best_score_straight[0:1])):
        best_score = best_score_multiple
    else:
        best_score = best_score_straight
    if (int(best_score[0:1]) < int(best_score_flush[0:1])):
        best_score = best_score_flush
    if (best_score_flush == "914"):
        best_score = "10"

    best_score = padRanking(best_score)
    return best_score

#UNFINISHED
#Function to rank who has the best hand at the end of a round
#Make scalable later, for now 4 players
def handRanking(player_vector, pool, winner):

    player_vector_index = 0
    hand_rankings = {}

    while (player_vector_index < len(player_vector)):
        #If players have reached the end of the final betting phase
        if (player_vector[player_vector_index].getStatus() == 1):
            hand_vec = player_vector[player_vector_index].getHand()
            hand_vec[2] = pool[0]
            hand_vec[3] = pool[1]
            hand_vec[4] = pool[2]
            hand_vec[5] = pool[3]
            hand_vec[6] = pool[4]
            hand_rankings[player_vector_index] = classifyHand(hand_vec)
        player_vector_index += 1

    print(hand_rankings)
    best_hand = {}
    best_hand_index = 0
    best_hand[0] = hand_rankings[0]
    best_hand[1] = "0"
    best_hand[2] = "0"
    best_hand[3] = "0"

    #Double loop to compare each letter of each classification
    winner_index = 0
    winner[0] = 0
    for i in range(1, len(hand_rankings)):
            if (int(best_hand[0]) < int(hand_rankings[i])):
                print("winner = " + str(winner))
                print("reached if statement")

                best_hand[0] = hand_rankings[i]
                best_hand[1] = 0
                best_hand[2] = 0
                best_hand[3] = 0

                winner[0] = i
                winner[1] = 0
                winner[2] = 0
                winner[3] = 0

                best_hand_index = 0
            if (int(best_hand[0]) == int(hand_rankings[i])):
                best_hand_index += 1
                best_hand[best_hand_index] = hand_rankings[i]
                winner_index += 1
                winner[winner_index] = i

    return best_hand
