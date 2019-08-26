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

def main():
    print("Welcome to Jojo's Blackjack Corner!!")
    print("")

    player_number = input("How many players(2-6)? ")

    if (player_number == "quit"):
        print("Thankyou for playing, Goodbye!")
        exit(0)

    PLAYER_NUMBER = int(player_number)

    while (PLAYER_NUMBER < 1 or PLAYER_NUMBER > 6):
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
    if (PLAYER_NUMBER == 1):
        Player1 = player.Player(player_money, "Player1", 0)
        player_vector[0] = Player1
        Player2 = player.Player(player_money, "Player2", 0)
        player_vector[1] = Player2
    elif (PLAYER_NUMBER == 2):
        Player1 = player.Player(player_money, "Player1", 0)
        player_vector[0] = Player1
        Player2 = player.Player(player_money, "Player2", 0)
        player_vector[1] = Player2
        Player3 = player.Player(player_money, "Player3", 0)
        player_vector[2] = Player3
    elif (PLAYER_NUMBER == 3):
        Player1 = player.Player(player_money, "Player1", 0)
        player_vector[0] = Player1
        Player2 = player.Player(player_money, "Player2", 0)
        player_vector[1] = Player2
        Player3 = player.Player(player_money, "Player3", 0)
        player_vector[2] = Player3
        Player4 = player.Player(player_money, "Player4", 0)
        player_vector[3] = Player4
    elif (PLAYER_NUMBER == 4):
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
        Player6 = player.Player(player_money, "Player6", 0)
        player_vector[5] = Player6
    user_input = ""

    while (True):
        user_input = input("Ready to play?")

        if (user_input == "quit"):
            print("Thank you for playing!")

        print("You have $" + str(Player1.getMoney()))

        card1 = draw(deck, cards_dealt)
        card2 = draw(deck, cards_dealt)
        card3 = draw(deck, cards_dealt)
        card4 = draw(deck, cards_dealt)

        Player1.setHand(card2, card4)
        Player2.setHand(card1, card3)

        user_input = int(input("How much are you betting (100, 500, or 1000)?"))

        while (user_input > Player1.getMoney()):
            user_input = int(input("Please enter a valid bet:"))

        pot = 2*actions.bet(user_input)

        player_hand = Player1.getHand()
        print("Hidden: First card is " + player_hand[0].getName())
        print("Visible: Second card is " + player_hand[1].getName())
        user_input = input("Would you like to hit or stay? ")
        if (user_input == "quit"):
            print("Thankyou for playing, goodbye!")
            exit(0)
        if (user_input == "hit"):
            hit(Player2)
        if (user_input == "stay"):
            print("Your total is " + total)
        dealer(Player1)
        
        print("\n \n \n \n \n \n \n \n\n \n \n \n \n \n \n \n \n \n \n \n \n \n" + Player.getName() + "'s turn!")

main()

