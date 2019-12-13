# Starting out with Python 
# Fourth Edition
# Tony Gaddis // Pearson

# Here's my solution to exercise #1 from chapter 11.
# Note that this Class file should be paired with the 
# Object file skb941/COP2510/ch11-1-productionworker.py
#
# Employee and ProductionWorker Classes:
# Write and Employee class that keeps data attributes for the following pieces of information:
# -Employee name
# -Employee number
# Next, write a class named ProductionWorker that is a subclass of the Employee class.
# The ProductionWorker class should keep data attributes for the following information:
# -Shift number (an integer, such as 1, 2, or 3)
# -Hourly pay rate
# The workday is divided into two shifts: day and night. The shift attribute will hold an 
# integer value representing the shift that the employee works. The day shift is shift 1
# and the night shift is shift 2. Write the appropriate accessor and mutator methods for each class.
#
# Once you have written the classes, write a program that creates an object of the Productionworker
# class and prompts the user to enter data for each of the object's data attributes. Store the data
# in the object, then use the object's accessor methods to retrieve it and display it on the screen.

# Employee class.
class Employee:
    
    # Initialize the object.
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    # Mutators.
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    # Accessors.
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

# ProductionWorker class.
class ProductionWorker(Employee):
    
    #Initialize the object.
    def __init__(self, name, number, shift, rate):
        # Call the superclass __init__ method.
        Employee.__init__(self, name, number)
        # Intialize the specialized attributes.
        self.__shift = shift
        self.__rate = rate

    # Mutators.
    def set_shift(self, shift):
        self.__shift = shift

    def set_rate(self, rate):
        self.__rate = rate

    # Accessors.
    def get_shift(self):
        return self.__shift

    def get_rate(self):
        return self.__rate

