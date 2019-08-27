#!/usr/bin/python3
import cards
import math
import random
import player

#UNFINISHED
#This function defines move at every step of the game
def move(Player, previous):
    print("\n \n \n \n \n \n \n \n\n \n \n \n \n \n \n \n \n \n \n \n \n \n" + Player.getName() + "'s turn!")
    player_hand = Player.getHand()
    user_input = input("Are you ready "+ Player.getName() + "?")
    print("First card is " + player_hand[0].getName())
    print("Second card is " + player_hand[1].getName())
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


def bet(Player, amount_bet):
    Player.setMoney(amount_bet, -1)


#This function defines the bet move
def hit(Player, hand_index):
    Player.hand[hand_index] = cards.draw()


#UNFINISHED
#This function defines reraise(may not be used)
def stay(Player, amount, amount_bet):
    while (amount > Player.getMoney() or amount < amount_bet):
        amount = int(input("Please enter a valid amount: "))
    #Player cannot bet less than big blind
    #Change later from 1
    Player.setMoney(amount, -1)
    return amount

#Needs testing
#This function defines the end of the round in which someone has won
def endRound(Player, amount_bet, busted, dealer):
    if (busted and dealer):
        Player.setMoney(amount_bet, 1)
        print(Player.getName() + " won $" + str(amount_bet))
    else:
        print("You lost $" + str(amount_bet))
