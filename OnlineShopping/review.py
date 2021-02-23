"""Implement your Review class in this file!"""
class Review:
    def __init__(self, description, user, product):
        self.desc = description
        self.user = user
        self.product = product
        
    def __str__(self):
        return f'Description:{self.desc}, User:{self.user}, Product:{self.product}'
