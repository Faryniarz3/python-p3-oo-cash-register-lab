#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount =  discount
    self.total = 0
    self.items = []
    self.transactions = []

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    self.transactions.append([title, price, quantity])

    for i in range(quantity):
      self.items.append(title)

  def apply_discount(self):

    if self.discount >0:
      self.total *= (1-self.discount / 100)
      self.total = int(self.total)
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    quantity = self.transactions[-1][2]
    price = self.transactions[-1][1]
    self.total -= quantity * price
    self.items = self.items[:-quantity]
    self.transactions = self.transactions[:-1]