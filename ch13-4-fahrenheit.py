# Starting out with Python 
# Fourth Edition
# Tony Gaddis // Pearson

# Here's my solution to exercise #4 from chapter 13.
#
# Celsius to Fahrenheit:
# Write a GUI program that convers Celsius temperatures to Fahrenheit temperatures.
# The user should be able to enter a Celsius temperature, click a button, then see 
# the equivalent Fahrenheit temperature. Use the following formula to make the conversion:
# F = C * 9 / 5 + 32
# F is the Fahrenheit temperature, and C is the Celsius temperature.

import tkinter

class FahrenheitGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create three frames to hold the widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Widgets for the top frame.
        self.celsius_label = tkinter.Label(self.top_frame,
                            text="Enter temperature in Celsius:")
        self.celsius_entry = tkinter.Entry(self.top_frame,
                                        width=10)
        

        # Pack the top frame's widgets.
        self.celsius_label.pack(side="left")
        self.celsius_entry.pack(side="left")

        # Create the middle frame's widgets.
        self.fahrenheit_label = tkinter.Label(self.middle_frame,
                            text="Fahrenheit temperature:")

        # Create StringVar for the output label.
        self.value = tkinter.StringVar()

        # Label for the StringVar object.
        self.converted_label = tkinter.Label(self.middle_frame,
                                textvariable = self.value)

        # Pack the middle frame's widgets.
        self.fahrenheit_label.pack(side="left")
        self.converted_label.pack(side="left")

        # Create the bottom frame's widgets.
        self.convert_button = tkinter.Button(self.bottom_frame,
                              text="Convert to Fahrenheit",
                              command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                           text="Quit",
                           command=self.main_window.destroy)

        # Pack the bottom frame's widgets.
        self.convert_button.pack(side="left")
        self.quit_button.pack(side="left")

        # Pack the frames.
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # Build the conversion method.
    def convert(self):
        C = float(self.celsius_entry.get())

        # Convert Celsius to Fahrenheit.
        F = C * 9 / 5 + 32

        # Convert F to a string and store it.
        self.value.set(F)

# Create an instance of the FahrenheitGUI class.
temp_conv = FahrenheitGUI()



                                        
        
