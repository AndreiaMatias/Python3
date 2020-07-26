# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 19:26:33 2020

@author: deiam
"""


""""Create a class to represent a bank account. 
It will need to have a balance a method of
withdrawing money, depositing money and 
displaying the balance to the screen. 
Create an instance of the bank account
and check that the methods work as expected."""

class bank_account(object):
    
    def __init__(self, balance=0.0):
        self.balance = balance
    
        
    def display_balance(self):
        print(f"Your balance is {self.balance}")
    def withdraw(self):
        amount = float(input("How much would you like to withdraw? >"))
        if amount < self.balance:
            self.balance -= amount
            print(f"Withdraw successful. Your balance is {self.balance}.")
        else:
            print(f"There's not enough money to withdraw. Your balance is {self.balance}")

    def deposit(self):
        amount = float(input("How much would you like to deposit? >"))
        self.balance += amount
        print(f"Deposit successful.")
        
        
savingsaccount = bank_account(300
                              )