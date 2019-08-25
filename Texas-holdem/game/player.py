#!/usr/bin/python3

class Player:
    """The player class is used to represent a player that is in the game.

    Attributes:
        money: An integer representing each amount of money that each player
        hand: A vector with 2 card objects representing the hand of player in a
            given round
        name: A string representation to differentiate trackers
        status: int whether a player is in a round or not (0 or 1)
    """

    def __init__(self, money, name, status):
        """Initializes Player class with money, name, and status."""
        self.money = money
        self.hand = {}
        self.name = name
        self.status = status

    #Function that allows the money of a player to be retrieved
    def getName(self):
        """Returns the name of a given player"""
        return self.name

    #Function that allows the money of a player to be retrieved
    def getMoney(self):
        """Returns the amount of money of a given player"""
        return self.money

    #Function that allows the money of a player to be changed
    def setMoney(self, amount, adjustment):
        """Sets the amount of money a player has"""
        if (adjustment == 0):
            self.money = amount
        if (adjustment == 1):
            self.money = self.getMoney() + amount
        if (adjustment == -1):
            self.money = self.getMoney() - amount

    #Function that allows the hand of a player to be retrieved
    def getHand(self):
        """Returns the hand vector of a player"""
        return self.hand

    #Function that allows to the hand of a player to be reset
    def setHand(self, card1, card2):
        """Sets the hand vector of a player"""
        self.hand[0] = card1
        self.hand[1] = card2

    #Function to get status
    def getStatus(self):
        """Returns the status of a player"""
        return self.status

    #Function to set status
    def setStatus(self, status):
        """Sets the status of a player"""
        self.status = status
