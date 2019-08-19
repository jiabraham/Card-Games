#!/usr/bin/python3

#DONE
#Define class Player
class Player:
    def __init__(self, money, name, status):
        self.money = money
        self.hand = {}
        self.name = name
        self.status = 0
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
            self.money = self.getMoney() + amount
        if (adjustment == -1):
            self.money = self.getMoney() - amount

    #Function that allows the hand of a player to be retrieved
    def getHand(self):
        return self.hand

    #Function that allows to the hand of a player to be reset
    def setHand(self, card1, card2):
        self.hand[0] = card1
        self.hand[1] = card2

    #Function to get status
    def getStatus(self):
        return self.status

    #Function to set status
    def setStatus(self, status):
        self.status = status
