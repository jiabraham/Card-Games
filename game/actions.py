#!/usr/bin/python3
import math
import random
import player

#UNFINISHED
#This function defines move at every step of the game
def move(Player, previous):
    print("\n \n \n \n \n \n \n \n\n \n \n \n \n \n \n \n \n \n \n \n \n \n" + Player.getName() + "'s turn!")
    player_hand = Player.getHand()
    user_input = input("Are you ready "+ Player.getName() + "?")
    print("First card is " + player_hand[0])
    print("Second card is " + player_hand[1])
    user_input = input("Would you like to check, bet, or fold? ")
    if (user_input == "quit"):
        print("Thankyou for playing, goodbye!")
        exit(0)
    if (user_input == "bet"):
        move = 1
        amount_bet = int(input("How much would you like to wager? "))
        amount_bet = actions.bet(Player1, amount_bet)
        pot = amount_bet
        print("Player1 has $" + str(Player1.getMoney()) + " left")
        print("Pot is now $" + str(pot))
        return amount
    if (user_input == "fold"):
        return -1
    if (user_input == "check"):
        return 0


#This function defines the bet move
def bet(Player, amount):
    while (amount > Player.getMoney() or amount < 1):
        amount = int(input("Please enter a valid amount: "))
    #Player cannot bet less than big blind
    #Change later from 1
    Player.setMoney(amount, -1)
    return amount


#This function defines reraise(may not be used)
def reraise(Player, amount, amount_bet):
    while (amount > Player.getMoney() or amount < amount_bet):
        amount = int(input("Please enter a valid amount: "))
    #Player cannot bet less than big blind
    #Change later from 1
    Player.setMoney(amount, -1)
    return amount

#UNFINISHED, needs testing
#This function defines the end of the round in which someone has won
def endRound(pool, player_vector, more_than_one_player, pot):
    if (more_than_one_player):
        winning_hand = cards.handRanking(player_vector, pool)
    else:
        player_vector_index = 0
        while (True):
            if (player_vector[player_vector_index].getStatus == 1):
                print(player_vector[player_vector_index].getName() + " wins $" + str(pot) + "!")
                break
