# Starting out with Python 
# Fourth Edition
# Tony Gaddis // Pearson

# Here's my solution to exercise #1 from chapter 10.
# Note that this Object file should be paired with the 
# Class file skb941/COP2510/pet.py
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

import pet

# Create an instance of the class.
my_pet = pet.Pet("", "", 0)

# Get pet data from user input.
name = input("What is your pet's name? ")
animal_type = input("What type of animal is that? ")
age = input("How old is your pet? ")

# Assign values based on input.
my_pet.set_name(name)
my_pet.set_animal_type(animal_type)
my_pet.set_age(age)

# Output the pet data.
print("Here is the information we have on file for your pet:")
print("Pet name:", my_pet.get_name())
print("Animal type:", my_pet.get_animal_type())
print("Age:", my_pet.get_age())
