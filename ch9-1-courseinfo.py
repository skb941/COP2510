# Starting out with Python 
# Fourth Edition
# Tony Gaddis // Pearson

# Here's my solution to exercise #1 from chapter 9.
#
# Write a program that creates a dictionary containing course numbers and 
# the room numbers of the rooms where the courses meet. The dictionary should
# have the following key-value pairs:
#
# Course Number (key)   Room Number (value)
# CS101                 3004
# CS102                 4501
# CS103                 6755
# NT110                 1244
# CM241                 1411
#
# The program should also create a dictionary containing course numbers and
# the names of the instructors that teach each course. The dictionary should 
# have the following key-value pairs:
#
# Course Number (key)   Instructor (value)
# CS101                 Haynes
# CS102                 Alvarado
# CS103                 Rich
# NT110                 Burke
# CM241                 Lee
# 
# The program should also create a dictionary containing course numbers and
# the meeting times for each course. The dictionary should have the following
# key-value pairs:
#
# Course Number (key)   Meeting Time (value)
# CS101                 8:00 a.m.
# CS102                 9:00 a.m.
# CS103                 10:00 a.m.
# NT110                 11:00 a.m.
# CM241                 1:00 p.m.
#
# The program should let the user enter a course number, then it should display
# the course's room number, instructor, and meeting time.


# Build the dictionaries.
room = {'CS101':'3004', 'CS102':'4501', 'CS103':'6755', 'NT110':'1244',\
        'CM241':'1411'}
instructor = {'CS101':'Haynes', 'CS102':'Alvarado', 'CS103':'Rich',\
              'NT110':'Burke', 'CM241':'Lee'}
time = {'CS101':'8:00 a.m.', 'CS102':'9:00 a.m.', 'CS103':'10:00 a.m.',\
        'NT110':'11:00 a.m.', 'CM241':'1:00 p.m.'}

def main():

# Get course number input from user.
    courseInput = input("Enter a course number: ")
    
    # Output info based on course number.
    if courseInput.upper() == "CS101":
        print("Room:",room.get('CS101')),\
        print("Instructor:",instructor.get('CS101')),\
        print("Time:",time.get('CS101'))

    if courseInput.upper() =="CS102":
        print("Room:",room.get('CS102')),\
        print("Instructor:",instructor.get('CS102')),\
        print("Time:",time.get('CS102'))
        
    if courseInput.upper() =="CS103":
        print("Room:",room.get('CS103')),\
        print("Instructor:",instructor.get('CS103')),\
        print("Time:",time.get('CS103'))

    if courseInput.upper() =="NT110":
        print("Room:",room.get('NT110')),\
        print("Instructor:",instructor.get('NT110')),\
        print("Time:",time.get('NT110'))

    if courseInput.upper() =="CM241":
        print("Room:",room.get('CM241')),\
        print("Instructor:",instructor.get('CM241')),\
        print("Time:",time.get('CM241'))

    if courseInput.upper() not in room:
        print("Course number not found.")

main()
