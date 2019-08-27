#!/usr/bin/python3

#DONE
#Define class Player
class Player:
    def __init__(self, money, name, status):
        self.money = money
        self.hand = {}
        self.name = name
        self.total = 0

    #Function that allows the money of a player to be retrieved
    def getName(self):
        return self.name

    #Function that allows the money of a player to be retrieved
    def getMoney(self):
        return self.money

    #Function that allows the money of a player to be changed
    def setMoney(self, amount, adjustment):
        if (adjustment == 0):
            self.money = amount
        if (adjustment == 1):
            self.money = self.getMoney() + int(amount)
        if (adjustment == -1):
            self.money = self.getMoney() - int(amount)

    #Function that allows the hand of a player to be retrieved
    def getHand(self):
        return self.hand

    #Function that allows to the hand of a player to be reset
    def setHand(self, card1, card2):
        self.hand[0] = card1
        self.hand[1] = card2

    #Function to get total
    def getTotal(self):
        return self.total

    #Function to set total
    def setTotal(self, total):
        self.total = total

    #Function to adjust total
    def adjustTotal(self, total):
        self.total += total
