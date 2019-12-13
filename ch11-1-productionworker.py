# Starting out with Python 
# Fourth Edition
# Tony Gaddis // Pearson

# Here's my solution to exercise #1 from chapter 11.
# Note that this should be paired with the Employee Class 
# file from skb941/COP2510/employee.py
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

import employee

# Input employee information.
name = input("Employee Name: ")
number = input("Employee Number: ")
rate = float(input("Rate of Pay: "))
shift = int(input("Shift: "))   

# Loop to determine if shift is valid.
while True: 
    if shift == "1":
        shift = "Day Shift"
        break
    elif shift == "2":
        shift = "Night Shift"
        break
    else:
        print("Invalid shift. Enter 1 for Day Shift or 2 for Night Shift.")
        shift = input("Shift: ")

# Create instance of ProductionWorker class.
production_worker = employee.ProductionWorker(name, number, shift, rate)

# Output object's data.
print("Employee Information")
print("********************")
print("Employee Name: ", production_worker.get_name(), sep="")
print("Employee Number: ", production_worker.get_number(), sep="")
print("Rate of Pay: ", "$", production_worker.get_rate(), sep="")
print("Employee Shift: ", production_worker.get_shift(), sep="")

