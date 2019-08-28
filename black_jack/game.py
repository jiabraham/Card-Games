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
        print("\n \n \n \n \n \n \n \n\n \n \n \n \n \n \n \n \n \n \n \n")

        user_input = input("Ready to play?")

        if (user_input == "quit" or user_input == "q"):
            print("Thank you for playing!")
            exit(0)

        print("You have $" + str(Player2.getMoney()))

        card1 = cards.draw(deck, cards_dealt)
        card2 = cards.draw(deck, cards_dealt)
        card3 = cards.draw(deck, cards_dealt)
        card4 = cards.draw(deck, cards_dealt)

        cards.resetHands(Player1)
        cards.resetHands(Player2)
        Player1.setHand(card2, card4)
        Player2.setHand(card1, card3)

        Player1.setTotal(card2.getClassification()+card4.getClassification())
        Player2.setTotal(card1.getClassification()+card3.getClassification())


        amount_bet = int(input("How much are you betting (100, 500, or 1000)?"))

        while (amount_bet > Player2.getMoney()):
            amount_bet = int(input("Please enter a valid bet:"))
        actions.bet(Player2, amount_bet)

        aces = 0
        busted = False
        hand_index = 2
        while (True):
            for i in range(0, len(Player2.hand)):
                if (i == 0):
                    print("Hidden: " + Player2.hand[i].getName())
                    if (Player2.hand[i].getClassification() == 11):
                        aces += 1
                else:
                    print("Visible: " + Player2.hand[i].getName())
                    if (Player2.hand[i].getClassification() == 11):
                        aces += 1
            if (len(Player2.hand) == 2 and Player2.getTotal() == 21):
                print("Blackjack, congradulations!")
                break;
            elif (Player2.getTotal() == 21):
                print("You got 21, congradulations!")
                break
            else :
                print("Your total is now: " + str(Player2.getTotal()))
            user_input = input("Would you like to hit or stay? ")
            if (user_input == "quit" or user_input == "q"):
                print("Thankyou for playing, goodbye!")
                exit(0)
            if (user_input == "hit"):
                Player2.hand[hand_index] = cards.draw(deck, cards_dealt)
                Player2.adjustTotal(Player2.hand[hand_index].getClassification())
                if (Player2.hand[hand_index].getClassification() == 11):
                    aces += 1
                hand_index += 1

                if (Player2.getTotal() > 21 and aces > 0):
                    print("print reached if statement")
                    cards.aceHighOrLow(Player2)
                print("Your total is now: " + str(Player2.getTotal()))

                if (Player2.getTotal() > 21):
                    print("Oops, busted")
                    for i in range(0, len(Player2.hand)):
                        if (i == 0):
                            print("Hidden: " + Player2.hand[i].getName())
                        else:
                            print("Visible: " + Player2.hand[i].getName())
                    busted = True
                    actions.endRound(Player2, amount_bet, busted, False)
                    break
            if (user_input == "stay"):
                print("Your total is " + str(Player2.getTotal()))
                break
        if (busted):
            continue
        dealer_total = 0
        hand_index = 2
        while(True):
            print("\nDealer's cards")

            for i in range(0, len(Player1.hand)):
                if (i == 0):
                    print("Hidden: " + Player1.hand[i].getName())
                    aces += 1
                else:
                    print("Visible: " + Player1.hand[i].getName())
                    aces += 1
            #INCREMENT ACE COUNT PROPERLY
            if (Player1.getTotal() < 17):
                Player1.hand[hand_index] = cards.draw(deck, cards_dealt)
                Player1.adjustTotal(Player1.hand[hand_index].getClassification())
                hand_index += 1
                print("\nLength of dealer hand = " + str(len(Player1.hand)))
                print("Hit")
                for i in range(0, len(Player1.hand)):
                    if (i == 0):
                        print("Hidden: " + Player1.hand[i].getName())
                    else:
                        print("Visible: " + Player1.hand[i].getName())
                print("Dealer total is now: " + str(Player1.getTotal()))
                continue

            if (Player1.getTotal() > 21 and aces > 0):
                print("print reached if statement")
                cards.aceHighOrLow(Player1)

            if (Player1.getTotal() == Player2.getTotal()):
                print("PUSH!!!")
                Player2.setMoney(amount_bet, 1)
                break

            if (Player1.getTotal() > 16 and Player1.getTotal() < 22):
                print("Dealer total is now: " + str(Player1.getTotal()))
                if (Player2.getTotal() > Player1.getTotal()):
                    print("You win $" + str(amount_bet) + "!")
                    increment = 2*amount_bet
                    Player2.setMoney(increment, 1)
                    break
                else:
                    print("You lose $" + str(amount_bet))
                    Player2.setMoney(amount_bet, -1)
                    break
                break
            if (Player1.getTotal() > 21):
                print("Dealer total is now: " + str(Player1.getTotal()))
                print("You win $" + str(amount_bet) + "!")
                amount_bet = 2*amount_bet
                Player2.setMoney(amount_bet, 1)
                break
        continue
        print(" \n \n \n \n \n \n \n \n \n \n \n" + Player.getName() + "'s turn!")

main()
