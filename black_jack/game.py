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
    print("\n \n \n \n \n \n \n \n\n \n \n \n \n \n \n \n \n \n \n \n \n \n")
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
    for i in range(0, PLAYER_NUMBER+1):
        player_vector[i] = player.Player(player_money, "Player" + str(i), 0)

    user_input = ""

    while (True):
        print("\n \n \n \n \n \n \n \n\n \n \n \n \n \n \n \n \n \n \n \n")

        user_input = input("Ready to play?")

        if (user_input == "quit" or user_input == "q"):
            print("Thank you for playing!")
            exit(0)

        print("You have $" + str(player_vector[1].getMoney()))

        card1 = cards.draw(deck, cards_dealt)
        card2 = cards.draw(deck, cards_dealt)
        card3 = cards.draw(deck, cards_dealt)
        card4 = cards.draw(deck, cards_dealt)

        cards.resetHands(player_vector[0])
        cards.resetHands(player_vector[1])
        player_vector[0].setHand(card2, card4)
        player_vector[1].setHand(card1, card3)

        player_vector[0].setTotal(card2.getClassification()+card4.getClassification())
        player_vector[1].setTotal(card1.getClassification()+card3.getClassification())


        amount_bet = int(input("How much are you betting (100, 500, or 1000)?"))

        while (amount_bet > player_vector[1].getMoney()):
            amount_bet = int(input("Please enter a valid bet:"))
        actions.bet(player_vector[1], amount_bet)

        aces = 0
        busted = False
        hand_index = 2
        while (True):
            for i in range(0, len(player_vector[1].hand)):
                if (i == 0):
                    print("Hidden: " + player_vector[1].hand[i].getName())
                    if (player_vector[1].hand[i].getClassification() == 11):
                        aces += 1
                else:
                    print("Visible: " + player_vector[1].hand[i].getName())
                    if (player_vector[1].hand[i].getClassification() == 11):
                        aces += 1
            if (len(player_vector[1].hand) == 2 and player_vector[1].getTotal() == 21):
                print("Blackjack, congradulations!")
                break;
            elif (player_vector[1].getTotal() == 21):
                print("You got 21, congradulations!")
                break
            else :
                print("Your total is now: " + str(player_vector[1].getTotal()))
            user_input = input("Would you like to hit or stay? ")
            if (user_input == "quit" or user_input == "q"):
                print("Thankyou for playing, goodbye!")
                exit(0)
            if (user_input == "hit"):
                player_vector[1].hand[hand_index] = cards.draw(deck, cards_dealt)
                player_vector[1].adjustTotal(player_vector[1].hand[hand_index].getClassification())
                if (player_vector[1].hand[hand_index].getClassification() == 11):
                    aces += 1
                hand_index += 1

                if (player_vector[1].getTotal() > 21 and aces > 0):
                    cards.aceHighOrLow(player_vector[1])
                print("Your total is now: " + str(player_vector[1].getTotal()))

                if (player_vector[1].getTotal() > 21):
                    print("Oops, busted")
                    for i in range(0, len(player_vector[1].hand)):
                        if (i == 0):
                            print("Hidden: " + player_vector[1].hand[i].getName())
                        else:
                            print("Visible: " + player_vector[1].hand[i].getName())
                    busted = True
                    actions.endRound(player_vector[1], amount_bet, busted, False)
                    break
            if (user_input == "stay"):
                print("Your total is " + str(player_vector[1].getTotal()))
                break
        if (busted):
            continue
        dealer_total = 0
        hand_index = 2
        while(True):
            print("\nDealer's cards")

            for i in range(0, len(player_vector[0].hand)):
                if (i == 0):
                    print("Hidden: " + player_vector[0].hand[i].getName())
                    aces += 1
                else:
                    print("Visible: " + player_vector[0].hand[i].getName())
                    aces += 1
            #INCREMENT ACE COUNT PROPERLY
            if (player_vector[0].getTotal() < 17):
                player_vector[0].hand[hand_index] = cards.draw(deck, cards_dealt)
                player_vector[0].adjustTotal(player_vector[0].hand[hand_index].getClassification())
                hand_index += 1
                print("\nLength of dealer hand = " + str(len(player_vector[0].hand)))
                print("Hit")
                for i in range(0, len(player_vector[0].hand)):
                    if (i == 0):
                        print("Hidden: " + player_vector[0].hand[i].getName())
                    else:
                        print("Visible: " + player_vector[0].hand[i].getName())
                print("Dealer total is now: " + str(player_vector[0].getTotal()))
                continue

            if (player_vector[0].getTotal() > 21 and aces > 0):
                print("print reached if statement")
                cards.aceHighOrLow(player_vector[0])

            if (player_vector[0].getTotal() == player_vector[1].getTotal()):
                print("PUSH!!!")
                player_vector[1].setMoney(amount_bet, 1)
                break

            if (player_vector[0].getTotal() > 16 and player_vector[0].getTotal() < 22):
                print("Dealer total is now: " + str(player_vector[0].getTotal()))
                if (player_vector[1].getTotal() > player_vector[0].getTotal()):
                    print("You win $" + str(amount_bet) + "!")
                    increment = 2*amount_bet
                    player_vector[1].setMoney(increment, 1)
                    break
                else:
                    print("You lose $" + str(amount_bet))
                    break
                break
            if (player_vector[0].getTotal() > 21):
                print("Dealer total is now: " + str(player_vector[0].getTotal()))
                print("You win $" + str(amount_bet) + "!")
                amount_bet = 2*amount_bet
                player_vector[1].setMoney(amount_bet, 1)
                break
        continue
        print(" \n \n \n \n \n \n \n \n \n \n \n" + Player.getName() + "'s turn!")

main()
