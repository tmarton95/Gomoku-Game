from tkinter import*
from tools.click_action import clicked

''' Define buttons as the game-board: '''
class GameBoard:
    def __init__(self):
        self.score_p1 = 0
        self.score_p2 = 0
        self.turn = 1
        self.clicked_buttons = []
        self.button_dict = {}

    def create_gameboard(self, window, LayoutProperties):
        row_num, column_num = [LayoutProperties.row_num, LayoutProperties.column_num]

        def on_enter(e):
            if self.turn < 0:
                e.widget['background'] = 'gray'
            else:
                e.widget['background'] = 'blue'

        def on_leave(e):
            e.widget['background'] = LayoutProperties.button_color

        # Create zeros matrix:
        self.game_matrix = [[0 for i in range(column_num)] for j in range(row_num)]

        for i in range(row_num):
            for j in range(column_num):
                name = f'button_{i}_{j}'
                self.button_dict[name] =  [Button(window, 
                                        width = 26, 
                                        height = 25, 
                                        bg = LayoutProperties.button_color, 
                                        image = LayoutProperties.virtualPixel, 
                                        borderwidth = 0.5, 
                                        relief = 'solid',
                                        command = lambda button_info=name: clicked(self, LayoutProperties, button_name=button_info)),
                                        [i, j]]

                self.button_dict[name][0].grid(row = i+2, column= j)
                self.button_dict[name][0].bind("<Enter>", on_enter)
                self.button_dict[name][0].bind("<Leave>", on_leave)
        
        # Define button for new game:
        button_new_game = Button(window, 
                            text = "New Game", 
                            font = ('Helvetia', 10), 
                            background = "orange",
                            height = 2, 
                            width = 16,
                            command = lambda: self.new_game(LayoutProperties))

        button_new_game.grid(row = 0, column = 14, columnspan = 18, rowspan = 2, sticky = 'e')

    # Define clear game-board for new game:
    def new_game(self, LayoutProperties):
        row_num, column_num = [LayoutProperties.row_num, LayoutProperties.column_num]
        for i in self.button_dict:
            self.button_dict[i][0].config(state = "normal", 
                                        bg = LayoutProperties.button_color, 
                                        image = LayoutProperties.virtualPixel, 
                                        borderwidth = 0.5, 
                                        relief = 'solid')

        self.game_matrix = [[0 for i in range(column_num)] for j in range(row_num)]
        self.clicked_buttons = []