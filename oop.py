# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    # Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)
    
    def boost(self):
        self.max_speed *= 2
        
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)
    
    def flame_jet(self,other):
        other.condition = "trashed"

#How does this solution demonstrate the four pillars of OOP?
#Encapsulation: the podracer class encapsulates the attributes max speed, condition, and price.
#Inheritance: The anakinspod and sebulbaspod class both innherit from the podracer class
#Polymorphism: Not found here I dont think
#Abstraction: The podracer class represents a podracer without showing how speed, condition, or price are handled. -
# - Anything using this class can use it without needing to know what or how its working "under the hood" so to speak.

#Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
#Technically yes, however since we are dealing with different types of podracers who share similar traits, OOP's coding style allows the code to be more organized and easy to read.

#How in particular did Object Oriented Programming assist in the solving of this problem?
#For me it helped me organize the parent class and its children. -
# - Because of the way its written I could easily update the parent class and reuse it for any future podracers I may want to create! -
# - However because I am not a starwars fan I do not see myself doing that anytime soon lol.
