# Starting out with Python 
# Fourth Edition
# Tony Gaddis // Pearson

# Here's my solution to exercise #1 from chapter 10.
# Note that this Class file should be paired with the 
# Object file skb941/COP2510/ch10-1-petclass.py
#
# Pet Class:
# Write a class named Pet, which should have the following data attributes:
# __name (for the name of the pet)
# __animal_type (for the type of animal that a pet is. Example values are 'Dog',
# 'Cat', and 'Bird')
# __age (for the pet's age)
#
# The pet class should have an __init__ method that creates these attributes. It
# should also have the following methods:
# set_name (This method assigns a value to the __name field.)
# set_animal_type (This method assigns a value to the __animal_type field.)
# set_age (This method assigns a value to the __age field.)
# get_name (This method returns the value of the __name field.)
# get_animal_type (This method returns the value of the __animal_type field.)
# get_age (This method returns the value of the __age field.)
#
# Once you have written the class, write a program that creates an object of the class 
# and prompts the user to enter the name, type, and age of his or her pet. This data 
# should be stored as the object's attributes. Use the object's accessor methods to 
# retrieve the pet's name, type, and age and display the data on the screen.

class Pet:

    # Initialize the attributes.
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # Set the pet's name.
    def set_name(self, name):
        self.__name = name

    # Set the pet's animal type.
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # Set the pet's age.
    def set_age(self, age):
        self.__age = age

    # Return the pet's name.
    def get_name(self):
        return self.__name

    # Return the pet's animal type.
    def get_animal_type(self):
        return self.__animal_type

    # Return the pet's age.
    def get_age(self):
        return self.__age
    
