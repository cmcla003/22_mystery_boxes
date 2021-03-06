from tkinter import *
from functools import partial # to prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        self.start_frame = Frame(padx=10,pady=10)
        self.start_frame.grid()

        #Mystery box heading (row 1)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game",
                                       font="Arial 18 bold")
        self.mystery_box_label.grid(row=1)


        # Entry Box (row 2)
        self.start_amount_entry = Entry(self.start_frame, font="Arial 16 bold")
        self.start_amount_entry.grid(row=2)

        # Play button
        self.lowstakes_button = Button(text="Low $5",
                                       command=lambda: self.to_game(1))
        self.lowstakes_button.grid(row=2, pady=10)

    def to_game(self,stakes):
        starting_balance = self.start_amount_entry.get()
        Game(self,stakes,starting_balance)

class Game:
    def __init__(self,partner,stakes,starting_balance):
        print(stakes)
        print(starting_balance)

        partner.lowstakes_button.config(state=DISABLED)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()
