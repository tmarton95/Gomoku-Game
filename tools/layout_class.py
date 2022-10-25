from tkinter import*

class Layout:
    def __init__(self, window):
        ''' Pictures for marks: '''
        self.x_icon = PhotoImage(file = "icons\\x_icon.png")
        self.x_icon_red = PhotoImage(file = "icons\\x_icon_red.png")
        self.o_icon= PhotoImage(file = "icons\\o_icon.png")
        self.o_icon_red= PhotoImage(file = "icons\\o_icon_red.png")
        self.virtualPixel = PhotoImage(file = "icons\\virtual_pix.png")

        self.x_icon_dark = PhotoImage(file = "icons\\x_icon_dark.png")
        self.o_icon_dark= PhotoImage(file = "icons\\o_icon_dark.png")
        
        ''' Labels on board: '''
        label_score = Label(window, text = "Scores:", font = ('Verdana', 12), pady = 10)
        label_score.grid(row = 0, column = 0, columnspan= 18, rowspan=2, sticky="w")

        label_p1 = Label(window, text = "Player 1:", font = ('Verdana', 10, 'bold'))
        label_p1.grid(row = 0, column = 3, columnspan = 18, sticky='w')

        label_p2 = Label(window, text = "Player 2:", font = ('Verdana', 10, 'bold'))
        label_p2.grid(row = 0, column = 6, columnspan = 18, sticky='w')

        self.label_p1_score = Label(window, text = "0", font = ('Verdana', 14, 'bold'))
        self.label_p1_score.grid(row = 1, column = 3, columnspan = 18, sticky='w', padx = 22)

        self.label_p2_score = Label(window, text = "0", font = ('Verdana', 14, 'bold'))
        self.label_p2_score.grid(row = 1, column = 6, columnspan = 18, sticky='w', padx = 22)

        self.label_turn = Label(window, text = "Player 1 turn:", font = ('Verdana', 10,))
        self.label_turn.grid(row = 0, column = 8, columnspan = 18, rowspan=2, sticky='w', padx = 22)

        self.label_turn_image = Label(window, image = self.x_icon)
        self.label_turn_image.grid(row = 0, column = 11, columnspan = 18, rowspan=2, sticky='w', padx = 33)