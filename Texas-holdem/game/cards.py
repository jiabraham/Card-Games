#!/usr/bin/python3
import math
import player
import random


class card:
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, name, classification):
        """Inits SampleClass with blah."""
        self.name = name
        self.classification = classification

    def getName(self):
        """Performs operation blah."""
        return self.name

    def setName(self, name):
        """Performs operation blah."""
        self.name = self.name + name

    def getClassification(self):
        """Performs operation blah."""
        return self.classification

    def setClassification(self, classification):
        """Performs operation blah."""
        self.classification = self.classification

#Function to create and set dictionary to hold cards
def setDeck():
    """This function sets the deck of cards within a constant read only vector.

    Returns:
        A dict mapping numbers 0-51 to the cards in a deck. Each row is
        represented as a tuple of strings. For example:

        {'0': ("Ace of Spades", 14)
         '10': ('10 of Spades', 10),
         '51': ('King of Diamonds', 51)}
    """
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
    """This function initializes the cards_dealt vector with all 0's.

    Returns:
        A dict mapping numbers 0-51 to a 0 or a 1. If the number maps to a 0,
        the card corresponding to that input is not in use. If the number
        maps to a 1, the card is in use and cannot be drawn again from
        the deck vector.
    """
    cards_dealt = {}
    for i in range (0, 52):
        cards_dealt[i] = 0
    return cards_dealt

#Function to draw a random card
def draw(deck, cards_dealt):
    """Fetches a card from the deck that has not already been drawn. This
        function adjusts the cards_dealt vector after finding a new card.

    Args:
        deck: a vector of the total possible 52 cards.
        cards_dealt: A vector of 1's and 0's indicating which cards have
            been already drawn.

    Returns:
        A new card from the deck to be used in the game, for example:

        Ace of Spades, 10 of Diamonds, 5 of Hearts
    """
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

def convertToMultiple(num):
    """This function converts a classification to a two digit number. 2 becomes
        02, 9 becomes 09, 12 stays as 12, if number is already two digits then
        it is left as is.

    Args:
        num: a classification of one of the cards in hand being ranked.

    Returns:
        The same number with padding if necessary

    """
    if (len(str(num)) != 2):
        num = "0" + str(num)
    else:
        num = str(num)
    return num

def padRanking(ranking):
    """This function converts a classification to a 5 digit number. 212 becomes
        21200, if number is already 5 digits then it stays as it is. This
        allows for greater than or less than comparison between rankings
        instead of comparing 1 or 2 digits at time.

    Args:
        ranking: an encoding of a ranking based on how good a hand is. The
            the higher the ranking, the better the hand is.

    Returns:
        A 5 digit ranking which can be directly compared to other rankings.
    """
    if (len(ranking) != 5):
        for i in range (0, 5-len(ranking)):
            ranking += "0"
    return ranking

def flush(hand_vec):
    """This function detects a flush within a hand vector of 7 cards. There are
        4 suits, each has a counter while looping through all 7 cards. After
        the 5th card, if there is 5 of a single suit, there exists flush.
        Additionally, after a flush is found, the vector needs to be
        checked for a straight to find out if there is a straight
        flush.

    Args:
        hand_vec: a vector of 7 cards that represents the hand of a player.

    Returns:
        A ranking indicating whether there is a flush, straight flush,
        or neither.
    """
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
    """This function detects a straight within a hand vector of 7 cards. A
        counter is kept and incremented if the next highest card is one
        greater than the previous card.

    Args:
        hand_vec: a vector of 7 cards that represents the hand of a player.

    Returns:
        A ranking indicating whether there is a straight or not.
    """
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
    """This function detects a pair, two pair, three of kind, full house, four
        of a kind within a hand vector of 7 cards. A histogram is calculated
        to determine how many of each classification exists within the hand.
        From this, all rankings involving cards with the same
        classification can be found.

    Args:
        hand_vec: a vector of 7 cards that represents the hand of a player.

    Returns:
        A ranking indicating whether there is any of the above types of
        hands.
    """
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
    """This function uses the previous 3 functions to classify the complete
        ranking of any given hand.

    Args:
        hand_vec: a vector of 7 cards that represents the hand of a player.

    Returns:
        The highest value among the 3 possible rankings of multiple, straight,
        and flush.
    """
    best_score = 0
    hand_vec = sortHand(hand_vec)

    best_score_multiple = multiple(hand_vec)
    best_score_straight = straight(hand_vec)
    best_score_flush = flush(hand_vec)

    if (int(best_score_multiple[0:1]) > int(best_score_straight[0:1])):
        best_score = best_score_multiple
    else:
        best_score = best_score_straight
    if (int(best_score[0:1]) < int(best_score_flush[0:1])):
        best_score = best_score_flush
    #Special binding for a royal flush
    if (best_score_flush == "914"):
        best_score = "10"

    best_score = padRanking(best_score)
    return best_score

#UNFINISHED
#Function to rank who has the best hand at the end of a round
#Make scalable later, for now 4 players
def handRanking(player_vector, pool, winner):
    """This function returns the best ranking of all hands being ranked at the
        end of round.

    Args:
        player_vector: a vector of all of the players in the round.
        pool: the cards that are common to everyone playing.
        winner: the index of the player that has the winning hand.

    Returns:
        The best hand among all players still in the round.
    """
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
