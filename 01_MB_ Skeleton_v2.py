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

        self.game_box = Toplevel()

        self.game_frame = Frame(self.game_box, padx=10, pady=10)
        self.game_frame.grid()
        # Heading (row 1)
        self.game_label = Label(self.game_frame, text="Heading",
                                       font="Arial 18 bold")
        self.game_label.grid(row=1)

        # Balance
        self.balance_label = Label(self.game_frame, text="Balance",
                                font="Arial 16 bold")
        self.balance_label.grid(row=2)

        # Gain
        self.gain_button = Button(self.game_frame,text="Gain",font="Arial 14 bold")
        self.gain_button.grid(row=3, pady=10)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()
