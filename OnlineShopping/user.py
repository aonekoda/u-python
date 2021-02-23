"""Implement your User class in this file!"""
from product import Product
from review import Review

class User:
    def __init__(self, id, name, reviews=[]):
        self.id = id
        self.name = name
        self.reviews = reviews
    
    def __str__(self):
        return f'ID:{self.id}, Name:{self.name}'
        
    def sell_product(self, product, description, price):
        return Product(product, description, self.name, [], price, True)
    
    def buy_product(self, product):
        if product.available :
            product.available = False
        
    def write_review(self, content, product):
        review = Review(content, self, product)
        product.reviews.append(review)
        self.reviews.append(review)
        return review
        
    
