#!/usr/bin/python3
import actions
import cards
import copy
import math
import player
import random


#Global variables, deck and cards_dealt vectors simulate a standard card deck
deck = cards.setDeck()
cards_dealt = cards.setCardsDealt()
#Welcome messages
#print("Welcome to Jojo's Poker Corner!!") something flashy
#Enter how many players

#Test hand ranking
# player_vec = {}
# player_money = 5000
# winner = {}
# Player1 = player.Player(player_money, "Player1", 1)
# player_vec[0] = Player1
# Player2 = player.Player(player_money, "Player2", 1)
# player_vec[1] = Player2
# Player3 = player.Player(player_money, "Player3", 1)
# player_vec[2] = Player3
#
# #declare hands
# card1 = cards.card("Ace of Spades", 14)
# card4 = cards.card("King of Diamonds", 13)
#
# card2 = cards.card("Ace of Diamonds", 14)
# card5 = cards.card("Jack of Hearts", 11)
#
# card3 = cards.card("King of Clubs", 13)
# card6 = cards.card("5 of Clubs", 5)
#
# #declare pool
# pool_test = {}
# pool_test[0] = cards.card("King of Hearts", 13)
# pool_test[1] = cards.card("Ace of Clubs", 14)
# pool_test[2] = cards.card("4 of Diamonds", 4)
# pool_test[3] = cards.card("Queen of Hearts", 12)
# pool_test[4] = cards.card("9 of Hearts", 9)
#
# Player1.setHand(card1, card4)
# Player2.setHand(card2, card5)
# Player3.setHand(card3, card6)
#
# best_score = cards.handRanking(player_vec, pool_test, winner)
# print(winner)
# print(best_score)


#UNFINISHED
#Actual game play
def main():
    player_number = input("How many players(2-6)? ")
    if (player_number == "quit"):
        print("Thankyou for playing, Goodbye!")
        exit(0)
    PLAYER_NUMBER = int(player_number)
    while (PLAYER_NUMBER < 2 or PLAYER_NUMBER > 6):
        PLAYER_NUMBER = int(input("Invalid input: "))
    #Enter how much money each player will have
    player_money = input("How much money will each player start out with? ")
    if (player_money == "quit"):
        print("Thankyou for playing, Goodbye!")
        exit(0)
    player_money = int(player_money)
    while (player_money < 1 or player_money > 1000000):
        player_number = int(input("Invalid input, please choose positive number from 1 to 1000000: "))
    print("Then let's get started!")

    #DONE
    #Player vector
    player_vector = {}
    #Declare number of players(loop through if you want after finished)
    if (PLAYER_NUMBER == 2):
        Player1 = player.Player(player_money, "Player1", 0)
        player_vector[0] = Player1
        Player2 = player.Player(player_money, "Player2", 0)
        player_vector[1] = Player2
    elif (PLAYER_NUMBER == 3):
        Player1 = player.Player(player_money, "Player1", 0)
        player_vector[0] = Player1
        Player2 = player.Player(player_money, "Player2", 0)
        player_vector[1] = Player2
        Player3 = player.Player(player_money, "Player3", 0)
        player_vector[2] = Player3
    elif (PLAYER_NUMBER == 4):
        Player1 = player.Player(player_money, "Player1", 0)
        player_vector[0] = Player1
        Player2 = player.Player(player_money, "Player2", 0)
        player_vector[1] = Player2
        Player3 = player.Player(player_money, "Player3", 0)
        player_vector[2] = Player3
        Player4 = player.Player(player_money, "Player4", 0)
        player_vector[3] = Player4
    elif (PLAYER_NUMBER == 5):
        Player1 = player.Player(player_money, "Player1", 0)
        player_vector[0] = Player1
        Player2 = player.Player(player_money, "Player2", 0)
        player_vector[1] = Player2
        Player3 = player.Player(player_money, "Player3", 0)
        player_vector[2] = Player3
        Player4 = player.Player(player_money, "Player4", 0)
        player_vector[3] = Player4
        Player5 = player.Player(player_money, "Player5", 0)
        player_vector[4] = Player5
    elif (PLAYER_NUMBER == 6):
        Player1 = player.Player(player_money, "Player1", 0)
        player_vector[0] = Player1
        Player2 = player.Player(player_money, "Player2", 0)
        player_vector[1] = Player2
        Player3 = player.Player(player_money, "Player3", 0)
        player_vector[2] = Player3
        Player4 = player.Player(player_money, "Player4", 0)
        player_vector[3] = Player4
        Player5 = player.Player(player_money, "Player5", 0)
        player_vector[4] = Player5
        Player6 = player.Player(player_money, "Player6", 0)
        player_vector[5] = Player6
    user_input = ""


    #Set game counter
    game_counter = 0
    while (user_input != "quit"):
        pot = 0
        player_vector_index = 0
        if (game_counter == 0):
            #Draws the hands of Players, puts them into a (player_number * 2) matrix
            #Later try to consolidate the 3 loops into 2
            hands = [["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""]]
            card_index = 0
            i = 0
            while (i < 2):
                card_index = 0
                while (card_index < PLAYER_NUMBER):
                    hands[card_index][i] = cards.draw(deck, cards_dealt)
                    card_index = card_index + 1
                i = i + 1

            #Sets the hands of all players using hands matrix
            #Sets the initial status to 1
            hand_index = 0
            while (hand_index < PLAYER_NUMBER):
                player_vector[player_vector_index].setHand(hands[hand_index][0], hands[hand_index][1])
                player_vector[player_vector_index].setStatus(1)
                hand_index = hand_index + 1
                player_vector_index = player_vector_index + 1

            #Starts game play
            #Initial round of betting before the flop
            players_moved = 0
            previous = -2
            player_vector_index = 0
            player_round_number = PLAYER_NUMBER
            while (players_moved != player_round_number):
                print(player_vector[player_vector_index].getName())
                round_bet = actions.move(player_vector[player_vector_index], previous)
                if (round_bet > 0):
                    pot = pot + round_bet
                    previous = round_bet
                    players_moved = 1
                elif (round_bet == 0):
                    previous = round_bet
                    players_moved = players_moved + 1
                elif (round_bet == -1):
                    previous = round_bet
                    player_round_number = player_round_number - 1
            if (player_round_number == 1):
                actions.endRound(player_vector, False)
                continue

        #if (game_counter == 1):
main()

