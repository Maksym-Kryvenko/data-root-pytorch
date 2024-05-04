# when to use class methods and when to use static methods?

class Item:
    
    @staticmethod
    def is_integer():
        '''
        This should do smth that has a relationship 
        with the class, but not smth that must be unique
        per instance!
        '''

    @classmethod
    def instantiate_from_something(cls):
        '''
        This should also do smth that has a relationship
        with the class, but usually, those are used to 
        manipulate different structures of data to instantiate
        objects, like we have done with CSV. 
        '''

# base principles of OOP: 
#   1. encapsulation - restricting the dirrect access to some of your attribute in the program (i.e. using read-only "__" and setters)
#   2. abstraction - show necessary and hide unnecessary attributes for user (i.e. hide methods that are required only inside "__")
#   3. inheritance - allow to reuse our code across the classes
#   4. polymorphism - refers to use of a single type entity to represent different types in different scenarios (i.e. using LEN function for string and list, it will work the same)
 