from tkinter import *


class App:
    def __init__(self):
        self.turn_label = None
        self.winner = None
        self.buttons = []
        self.button_frames = []
        self.game_list = [None] * 9
        self.main_panel = None
        self.start_button = None
        self.lower_frame = None
        self.player_1 = None
        self.player_2 = None
        self.turn = None
        self.button_bg_color = '#808080'
        self.bg_color = '#c0c0c0'
        self.entry_bg_color = '#f2f2f2'
        self.fg_color = '#000000'
        self.font = ('Cambria', 14)

    def restart(self):
        self.turn = None
        self.winner.set('Draw')
        self.game_list = [None] * 9
        for idx in range(9):
            self.buttons[idx].config(image='', state=NORMAL)

    def change_turn(self, idx):
        player_1 = PhotoImage(file=r'images/player_1.png')
        player_2 = PhotoImage(file=r'images/player_2.png').subsample(10)
        if self.turn is None:
            self.buttons[idx].config(image=player_1, state=DISABLED)
            self.buttons[idx].image = player_1
            self.game_list[idx] = 0
            self.turn = 2
            self.turn_label.config(text=f"{self.player_2.get()}'s Turn")
        elif self.turn == 1:
            self.buttons[idx].config(image=player_1, state=DISABLED)
            self.buttons[idx].image = player_1
            self.game_list[idx] = 0
            self.turn = 2
            self.turn_label.config(text=f"{self.player_2.get()}'s Turn")
        elif self.turn == 2:
            self.buttons[idx].config(image=player_2, state=DISABLED)
            self.buttons[idx].image = player_2
            self.game_list[idx] = 1
            self.turn = 1
            self.turn_label.config(text=f"{self.player_1.get()}'s Turn")
        self.check_winner()

    def check_winner(self):
        # check rows
        for i in range(3):
            if self.game_list[i*3:i*3+3] == [0]*3:
                self.winner.set(self.player_1.get())
            if self.game_list[i*3:i*3+3] == [1]*3:
                self.winner.set(self.player_2.get())

        # check columns
        for j in range(3):
            if [self.game_list[j], self.game_list[j+3], self.game_list[j+6]] == [0]*3:
                self.winner.set(self.player_1.get())
            if [self.game_list[j], self.game_list[j+3], self.game_list[j+6]] == [1]*3:
                self.winner.set(self.player_2.get())

        # check diagonals
        if [self.game_list[0], self.game_list[4], self.game_list[8]] == [0]*3:
            self.winner.set(self.player_1.get())
        if [self.game_list[0], self.game_list[4], self.game_list[8]] == [1]*3:
            self.winner.set(self.player_2.get())

        if [self.game_list[2], self.game_list[4], self.game_list[6]] == [0]*3:
            self.winner.set(self.player_1.get())
        if [self.game_list[2], self.game_list[4], self.game_list[6]] == [1]*3:
            self.winner.set(self.player_2.get())

        if self.winner.get() != 'Draw' or self.game_list.count(None) == 0:
            if self.winner.get() != 'Draw':
                message = f'{self.winner.get()} Won!'
            else:
                message = 'Game Draw!'
            winner_window = Toplevel(bg=self.bg_color)
            winner_window.title('Game Finish')
            logo = PhotoImage(file=r'images/logo.png')
            winner_window.iconphoto(False, logo)

            upper_frame = Frame(winner_window, bg=self.bg_color)
            Label(master=upper_frame,
                  bg=self.bg_color,
                  fg=self.fg_color,
                  font=self.font,
                  text=message).grid(row=0, column=0, columnspan=2, padx=10, pady=5)
            lower_frame = Frame(winner_window, bg=self.bg_color)
            Button(master=lower_frame,
                   bg=self.button_bg_color,
                   fg=self.fg_color,
                   font=self.font,
                   height=1,
                   text='Play Again',
                   command=lambda: [winner_window.destroy(), self.restart()]).grid(row=1, column=0, padx=10, pady=5)
            Button(master=lower_frame,
                   bg=self.button_bg_color,
                   fg=self.fg_color,
                   font=self.font,
                   height=1,
                   text='Close',
                   command=lambda: [self.main_panel.destroy()]).grid(row=1, column=1, padx=10, pady=5)

            upper_frame.pack(side='top')
            lower_frame.pack(side='top')
            winner_window.geometry('400x120')
            winner_window.grab_set()
            winner_window.mainloop()

    def run(self):
        self.main_panel = Tk()
        self.main_panel.title('Tic Tac Toe')
        logo = PhotoImage(file=r'images/logo.png')
        self.main_panel.iconphoto(False, logo)
        self.main_panel.config(bg=self.bg_color)

        upper_frame = Frame(self.main_panel, bg=self.bg_color)
        self.player_1 = StringVar()
        self.player_1.set('Player 1')
        self.player_2 = StringVar()
        self.player_2.set('Player 2')
        self.winner = StringVar()
        self.winner.set('Draw')

        Label(master=upper_frame,
              bg=self.bg_color,
              fg=self.fg_color,
              font=self.font,
              text='Enter the names of the players').grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        Label(master=upper_frame,
              bg=self.bg_color,
              fg=self.fg_color,
              font=self.font,
              text='Player 1').grid(row=1, column=0, padx=5, pady=5)
        Entry(master=upper_frame,
              textvariable=self.player_1,
              font=self.font,
              bd=5,
              bg=self.entry_bg_color,
              fg=self.fg_color,
              justify='right').grid(row=1, column=1, padx=5, pady=5)
        player_1 = PhotoImage(file=r'images/player_1.png').subsample(2)
        Label(master=upper_frame,
              bg=self.bg_color,
              fg=self.fg_color,
              font=self.font,
              image=player_1).grid(row=1, column=3, padx=5, pady=5)

        Label(master=upper_frame,
              bg=self.bg_color,
              fg=self.fg_color,
              font=self.font,
              text='Player 2').grid(row=2, column=0, padx=5, pady=5)
        Entry(master=upper_frame,
              textvariable=self.player_2,
              font=self.font,
              bd=5,
              bg=self.entry_bg_color,
              fg=self.fg_color,
              justify='right').grid(row=2, column=1, padx=5, pady=5)
        player_2 = PhotoImage(file=r'images/player_2.png').subsample(20)
        Label(master=upper_frame,
              bg=self.bg_color,
              fg=self.fg_color,
              font=self.font,
              image=player_2).grid(row=2, column=3, padx=5, pady=5)

        self.lower_frame = Frame(self.main_panel, bg=self.bg_color)
        self.start_button = Button(master=self.lower_frame,
                                   bg=self.button_bg_color,
                                   fg=self.fg_color,
                                   font=self.font,
                                   height=1,
                                   width=10,
                                   text='Start Game',
                                   command=lambda: [self.tic_tac_toe(), self.start_button.grid_forget()])
        self.start_button.grid(row=0, column=0, padx=5, pady=5)

        upper_frame.pack(side='top')
        self.lower_frame.pack(side='top', pady=20)
        self.main_panel.geometry('500x250')
        self.main_panel.mainloop()

    def tic_tac_toe(self):
        self.main_panel.geometry('500x450')
        idx = 0
        for row in range(3):
            for col in range(3):
                self.button_frames.append(Frame(self.lower_frame, height=65, width=64))
                self.button_frames[idx].propagate(False)
                self.button_frames[idx].grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
                self.buttons.append(Button(master=self.button_frames[idx],
                                           bg=self.button_bg_color,
                                           fg=self.fg_color,
                                           font=self.font,
                                           command=lambda i=idx: [self.change_turn(i)]))
                self.buttons[idx].pack(expand=True, fill=BOTH)
                idx += 1
        self.turn_label = Label(master=self.main_panel,
                                bg=self.bg_color,
                                font=self.font,
                                text=f"{self.player_1.get()}'s Turn")
        self.turn_label.pack(side='top')


if __name__ == "__main__":
    app_instance = App()
    app_instance.run()
