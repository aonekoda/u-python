# 클래스 데코레이터 @property, @classmethod
class Customer:
    def __init__(self, first, last, tier=('free',0)):
        self.firstname = first
        self.lastname = last
        self.tier = tier[0]
        self.cost = tier[1]
        
    def bill_for(self, mo):
        return self.cost * mo
    
    def can_access(self, content):
        return content['tier']=='free' or content['tier']==self.tier
    
    @property
    def name(self):
        return self.firstname + ' ' + self.lastname
    
    @classmethod
    def premium(cls, first, last):
        return cls(first, last, tier=('premium',10))

if __name__ == '__main__':
    # This won't run until you implement the `Customer` class!
    
    marco = Customer('Marco', 'Polo')  # Defaults to the free tier
    print(marco.name)  # Marco Polo
    print(marco.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
    print(marco.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # False

    victoria = Customer.premium("Alexandrina", "Victoria")  # Build a customer around the ('premium', 10$/mo) streaming plan.
    print(victoria.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
    print(victoria.can_access({'tier': 'premium', 'title': 'William Tell Overture'}))  # True
    print(victoria.bill_for(5))  # => 50 (5 months at 10$/mo)
    print(victoria.name)  # Alexandrina Victoria
