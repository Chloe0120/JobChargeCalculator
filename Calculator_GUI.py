# Chloe Chin 13COS
# 10th Oct 2022
# Version 1 - Calculator page (main) GUI skeleton

from tkinter import *
from functools import partial
import random
from PIL import ImageTk, Image

class job_information:
    def __init__(self, job_number, customer_name, distance_travelled,
                 time_spent, wof_and_tune, job_charge):
        self.job_number = job_number
        self.customer_name = customer_name
        self.distance_travelled = distance_travelled
        self.time_spent = time_spent
        self.wof_and_tune = wof_and_tune
        self.job_charge = job_charge

class Calculator:
    def __init__(self):

        # Formatting variables
        background_color = "gray92"

        # Calculator Frame
        self.calculator_frame = Frame(bg=background_color,
                                      pady=10)
        self.calculator_frame.grid()

        # Job Charge Calculator logo (row 0)
        self.image = Image.open("business_logo.png")
        self.image = self.image.resize((500, 100))
        self.business_logo_image = ImageTk.PhotoImage(self.image)
        self.business_logo_label = Label(self.calculator_frame,
                                         image=self.business_logo_image)
        self.business_logo_label.grid(row=0, padx= 20, pady=10)

        # User instructions (row 1)
        self.instructions_label = Label(self.calculator_frame,
                                        text="User instructions",
                                        font="Arial 10 italic", wrap=250,
                                        justify=LEFT, bg=background_color,
                                        padx=10, pady=10)
        self.instructions_label.grid(row=1)

        # Job number entry box (row 2)
        self.job_number_frame = Frame(self.calculator_frame,
                                      bg=background_color)
        self.job_number_frame.grid(row=2, pady=10)
        self.job_number_label = Label (self.job_number_frame,
                                       bg=background_color,
                                       text="Job number :",
                                       font="Arial 14")
        self.job_number_label.grid(row=0, column=0, padx=10)
        self.job_number_entry = Entry(self.job_number_frame)
        self.job_number_entry.grid(row=0, column=1)

        # Customer name entry box (row 3)
        self.customer_name_frame = Frame(self.calculator_frame,
                                         bg=background_color)
        self.customer_name_frame.grid(row=3, pady=10)
        self.customer_name_label = Label(self.customer_name_frame,
                                         bg=background_color,
                                         text="Customer name :",
                                         font="Arial 14")
        self.customer_name_label.grid(row=0, column=0, padx=10)
        self.customer_name_entry = Entry(self.customer_name_frame)
        self.customer_name_entry.grid(row=0, column=1)

        # Distance travelled entry box (row 4)
        self.distance_travelled_frame = Frame(self.calculator_frame,
                                              bg=background_color)
        self.distance_travelled_frame.grid(row=4, pady=10)
        self.distance_travelled_label = Label(self.distance_travelled_frame,
                                              bg=background_color,
                                              text="Distance travelled :",
                                              font="Arial 14")
        self.distance_travelled_label.grid(row=0, column=0, padx=10)
        self.distance_travelled_entry = Entry(self.distance_travelled_frame)
        self.distance_travelled_entry.grid(row=0, column=1)

        # Minutes spent on virus protection entry box (row 5)
        self.minutes_spent_frame = Frame(self.calculator_frame,
                                         bg=background_color)
        self.minutes_spent_frame.grid(row=5, pady=10)
        self.minutes_spent_label = Label(self.minutes_spent_frame,
                                         bg=background_color,
                                         text="Minutes spent on virus protection :",
                                         font="Arial 14")
        self.minutes_spent_label.grid(row=0, column=0, padx=10)
        self.minutes_spent_entry = Entry(self.minutes_spent_frame)
        self.minutes_spent_entry.grid(row=0, column=1, padx=(0, 10))

        # WOF and tune checkbox (row 6)
        self.wof_and_tune_frame = Frame(self.calculator_frame,
                                        bg=background_color)
        self.wof_and_tune_frame.grid(row=6, pady=10)
        self.wof_and_tune_label = Label(self.wof_and_tune_frame,
                                        bg=background_color,
                                        text="WOF and tune service was required :",
                                        font="Arial 14")
        self.wof_and_tune_label.grid(row=0, column=0, padx=10)
        self.wof_and_tune_checkbutton = Checkbutton(self.wof_and_tune_frame)
        self.wof_and_tune_checkbutton.grid(row=0, column=1)

        # Submit button (row 7), orchid3, khaki1
        self.to_submit_button = Button(self.calculator_frame,
                                       text="Submit", font="Arial 12 bold",
                                       bg="Khaki1", padx=10, pady=10)
        self.to_submit_button.grid(row=7, pady=10)

        # Job Charge label (row 8)
        self.job_charge_label = Label(self.calculator_frame, font="Arial 14 bold",
                                      bg=background_color, fg="RoyalBlue3",
                                      pady=10, text="Total job charge ($) : ")
        self.job_charge_label.grid(row=8, column=0)

        # History / Help button frame (row 9)
        self.calc_hist_button = Button(self.calculator_frame, font="Arial 12 bold",
                                       text="Calculation History",
                                       padx=10, pady=10)
        self.calc_hist_button.grid(row=9, pady=10)







if __name__ == "__main__":
    root = Tk()
    root.title("Job Charge Calculator")
    something = Calculator()
    root.mainloop()
