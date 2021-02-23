"""Implement your Product class in this file!"""


class Product :
    def __init__(self, name, description, seller, reviews, price, availability):
        self.name = name
        self.desc = description
        self.seller = seller
        self.reviews = reviews
        self.price = price
        self.available  = availability
        
    def __str__(self):
        return f'{self.name}, {self.desc}, {self.seller}, {self.reviews}, {self.price}, {self.available}'
    
