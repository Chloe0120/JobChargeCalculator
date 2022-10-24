# Chloe Chin 13COS
# 20th Oct 2022
# Version 6 - Display output on main & history page

from tkinter import *
from functools import partial
import re
import random
from PIL import ImageTk, Image


class Job:

    # Storing gathered data
    def __init__(self, job_number, customer_name, distance_travelled,
                 time_spent, wof_and_tune):
        self.job_number = job_number
        self.customer_name = customer_name
        self.distance_travelled = round(distance_travelled)
        self.time_spent = time_spent
        self.wof_and_tune = wof_and_tune
        self.job_charge = None
        self.calculation()

    def calculation(self):

        # Calculating travel fee
        # If distance travelled to customer is within 5km
        if self.distance_travelled <= 5:
            travel_fee = 10
        # If distance travelled to customer is over 5km
        else:
            travel_fee = (self.distance_travelled - 5) * 0.5 + 10
        # Testing if travel fee is correct
        print("travel fee :", travel_fee)

        # Calculating service fee
        # If provided service is Virus Protection Service
        if not self.wof_and_tune:
            service_fee = self.time_spent * 0.8
        # If provided service is WOF and tune service
        else:
            service_fee = 100
        # Testing if service fee is correct
        print("service fee :", service_fee)

        # Calculating total job charge
        self.job_charge = travel_fee + service_fee
        # Testing if total job charge is correct
        print("total job charge:", self.job_charge)


class Calculator:

    def __init__(self):

        # Formatting variables
        background_color = "grey92"
        self.job_list = []

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
        self.business_logo_label.grid(row=0, padx=20, pady=(10, 0))

        # User instructions (row 1)
        self.instructions_label = Label(self.calculator_frame,
                                        text="User instructions",
                                        font="Arial 10 italic",
                                        justify=LEFT, bg=background_color,
                                        padx=10, pady=30)
        self.instructions_label.grid(row=1)

        # Set up entries frame (row 2)
        self.entries_frame = Frame(self.calculator_frame, bg=background_color)
        self.entries_frame.grid(row=2)

        # Job number entry box
        self.job_number_label = Label(self.entries_frame,
                                      bg=background_color,
                                      text="Job number :",
                                      font="Arial 14")
        self.job_number_label.grid(row=0, column=0, padx=20, sticky=NE)
        self.job_number_entry = Entry(self.entries_frame,
                                      highlightbackground=background_color)
        self.job_number_entry.grid(row=0, column=1, padx=20)

        # Customer name entry box
        self.customer_name_label = Label(self.entries_frame,
                                         bg=background_color,
                                         text="Customer name :",
                                         font="Arial 14")
        self.customer_name_label.grid(row=1, column=0, padx=20, sticky=NE)
        self.customer_name_entry = Entry(self.entries_frame,
                                         highlightbackground=background_color)
        self.customer_name_entry.grid(row=1, column=1, padx=20)

        # Distance travelled entry box
        self.distance_travelled_label = Label(self.entries_frame,
                                              bg=background_color,
                                              text="Distance travelled :",
                                              font="Arial 14")
        self.distance_travelled_label.grid(row=2, column=0, padx=20, sticky=NE)
        self.distance_travelled_entry = Entry(self.entries_frame,
                                              highlightbackground=background_color)
        self.distance_travelled_entry.grid(row=2, column=1, padx=20)

        # Minutes spent on virus protection entry box
        self.minutes_spent_label = Label(self.entries_frame,
                                         bg=background_color,
                                         text="Minutes spent :",
                                         font="Arial 14")
        self.minutes_spent_label.grid(row=3, column=0, padx=20, sticky=NE)
        self.minutes_spent_entry = Entry(self.entries_frame,
                                         highlightbackground=background_color)
        self.minutes_spent_entry.grid(row=3, column=1, padx=20)

        # WOF and tune checkbox
        self.wof_and_tune_label = Label(self.entries_frame,
                                        bg=background_color,
                                        text="WOF and tune service :",
                                        font="Arial 14")
        self.wof_and_tune_label.grid(row=4, column=0, padx=20, pady=(30, 0), sticky=E)
        self.wofBoolean = BooleanVar(False)
        self.wof_and_tune_checkbutton = Checkbutton(self.entries_frame,
                                                    variable=self.wofBoolean,
                                                    bg=background_color)
        self.wof_and_tune_checkbutton.grid(row=4, column=1, padx=20, pady=(30, 0))

        # Submit button (row 7), orchid3, khaki1
        self.to_submit_button = Button(self.calculator_frame,
                                       text="Submit", font="Arial 12 bold",
                                       bg="Khaki1", padx=10, pady=10,
                                       highlightbackground=background_color,
                                       command=lambda: self.submit())
        self.to_submit_button.grid(row=7, pady=30)

        # Job Charge label (row 8)
        self.job_charge_label = Label(self.calculator_frame, font="Arial 14 bold",
                                      bg=background_color, fg="RoyalBlue3",
                                      text="Total job charge ($) : ")
        self.job_charge_label.grid(row=8, column=0)

        # History(Show All Jobs) button frame (row 9)
        self.history_button = Button(self.calculator_frame, font="Arial 12 bold",
                                     text="Show All Jobs", padx=10, pady=10,
                                     highlightbackground=background_color,
                                     command=lambda: self.history(self.job_list))
        self.history_button.grid(row=9, pady=30)

        if len(self.job_list) == 0:
            self.history_button.config(state=DISABLED)

    def submit(self):

        # Store job instance,
        job = Job(int(self.job_number_entry.get()),
                  self.customer_name_entry.get(),
                  float(self.distance_travelled_entry.get()),
                  int(self.minutes_spent_entry.get()),
                  self.wofBoolean.get()
                  )

        # Store job instance to list
        self.job_list.append(job)

        # Enable history button when job list is appended
        if len(self.job_list) > 0:
            self.history_button.config(state=NORMAL)

        # Configurate job charge label to display correct value
        self.job_charge_label.config(text="Total job charge ($) : " + str(self.job_list[-1].job_charge))

    def history(self, job_list):
        History(self, job_list)


class History:
    def __init__(self, partner, job_list):

        # disable history button when history window is activated
        partner.history_button.config(state=DISABLED)

        # Sets up child window (ie: history window)
        self.history_window = Toplevel()

        # If users press cross at top, closes history and 'releases' history button
        self.history_window.protocol('WM_DELETE_WINDOW',
                                     partial(self.close_history, partner))

        # Set up variables
        background_color = "grey92"

        # Set up history GUI frame
        self.history_frame = Frame(self.history_window, width=500,
                                   bg=background_color)
        self.history_frame.grid()
        # self.history_frame.place(relx=0.5, anchor=N)

        # Set up heading label (row 0)
        self.history_heading = Label(self.history_frame, text="Job history",
                                     font="arial 16 bold",
                                     bg=background_color)
        self.history_heading.grid(row=0, pady=(20, 10))

        # history instruction label (row 1)
        self.history_instruction = Label(self.history_frame,
                                         text="Here is your calculation history. "
                                              "you can use the next / previous button to "
                                              "move on to next / previous job information",
                                         wraplength=250,
                                         font="arial 12 italic",
                                         justify=LEFT, bg=background_color,
                                         padx=20, pady=10)
        self.history_instruction.grid(row=1)

        # Set variables for history output frame
        output_background_color = "white"
        self.current_index = -1

        # Set history output frame (row 2)
        self.history_output_frame = Frame(self.history_frame, bg=output_background_color)
        self.history_output_frame.grid(row=2, pady=20)

        # Set history output label
        self.job_number_label = Label(self.history_output_frame, text="Job number :",
                                      bg=output_background_color)
        self.job_number_label.grid(row=0, column=0, padx=20, pady=10, sticky=NW)

        self.customer_name_label = Label(self.history_output_frame, text="Customer name :",
                                         bg=output_background_color)
        self.customer_name_label.grid(row=1, column=0, padx=20, pady=10, sticky=NW)

        self.job_charge_label = Label(self.history_output_frame, text="Job charge :",
                                      bg=output_background_color)
        self.job_charge_label.grid(row=2, column=0, padx=20, pady=10, sticky=NW)

        # Call function to display history output

        #self.job_number = partner.job_list[self.current_index].job_number

        self.job_number_output = Label(self.history_output_frame,
                                       text=partner.job_list[self.current_index].job_number,
                                       bg=output_background_color)
        self.job_number_output.grid(row=0, column=1, padx=20, pady=10, sticky=W)

        self.customer_name_output = Label(self.history_output_frame,
                                          text=partner.job_list[self.current_index].customer_name,
                                          bg=output_background_color)
        self.customer_name_output.grid(row=1, column=1, padx=20, pady=10, sticky=W)

        self.job_charge_output = Label(self.history_output_frame,
                                       text=partner.job_list[self.current_index].job_charge,
                                       bg=output_background_color)
        self.job_charge_output.grid(row=2, column=1, padx=20, pady=10, sticky=W)

        print(len(partner.job_list))

        # Next / Previous button (row 3)
        self.next_previous_frame = Frame(self.history_frame, bg=background_color)
        self.next_previous_frame.grid(row=3, pady=20)

        # Previous button
        self.previous_button = Button(self.next_previous_frame, text="Previous",
                                      font="Arial 12 bold",
                                      highlightbackground=background_color,
                                      padx=10, pady=10, width=10,
                                      command=lambda: self.set_displayed_data(partner, "previous"))
        self.previous_button.grid(row=0, column=0, padx=(20, 80))

        # next button
        self.next_button = Button(self.next_previous_frame, text="Next",
                                  font="Arial 12 bold",
                                  highlightbackground=background_color,
                                  padx=10, pady=10, width=10,
                                  command=lambda: self.set_displayed_data(partner, "next"))
        self.next_button.grid(row=0, column=1, padx=(80, 20))

        # Call a function to check / change button state
        self.check_button_state(partner)

    def check_button_state(self, partner):
        # Disable both buttons if there's only one item
        if self.current_index + len(partner.job_list) == 0 and self.current_index == -1:
            self.previous_button.config(state=DISABLED)
            self.next_button.config(state=DISABLED)
            print(self.current_index)
        # Disable previous button if there's no more previous data
        elif self.current_index + len(partner.job_list) == 0:
            self.previous_button.config(state=DISABLED)
            print("1")
        # Disable next button if there's no more recent data
        elif self.current_index == -1:
            self.next_button.config(state=DISABLED)
            print("2")
        # Enable both buttons
        else:
            self.previous_button.config(state=NORMAL)
            self.next_button.config(state=NORMAL)
            print("3")

    def set_displayed_data(self, partner, navigate_to):
        if navigate_to == "previous":
            self.current_index -= 1
        else:
            self.current_index += 1
        self.job_number_output.config(text=partner.job_list[self.current_index].job_number)
        self.customer_name_output.config(text=partner.job_list[self.current_index].customer_name)
        self.job_charge_output.config(text=partner.job_list[self.current_index].job_charge)

        self.check_button_state(partner)

    def close_history(self, partner):
        # Enable history button and close the history window
        partner.history_button.config(state=NORMAL)
        self.history_window.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Job Charge Calculator")
    something = Calculator()
    root.mainloop()
