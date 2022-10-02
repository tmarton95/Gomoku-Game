from tkinter import*
from tools.click_action import clicked

class GameBoard():
    def __init__(self, window, row_num, column_num, score_p1, score_p2, LayoutProperties):
        self.row_num = row_num
        self.column_num = column_num
        self.score_p1 = score_p1
        self.score_p2 = score_p2
        self.turn = 1

        self.virtualPixel = LayoutProperties.virtualPixel
        
        self.game_matrix = [[0 for i in range(column_num)] for j in range(row_num)]
        self.clicked_buttons = []
        self.button_dict = {}

        def on_enter(e):
            if self.turn < 0:
                e.widget['background'] = 'gray'
            else:
                e.widget['background'] = 'blue'

        def on_leave(e):
            e.widget['background'] = 'lightblue'

        for i in range(row_num):
            for j in range(column_num):
                name = f'button_{i}_{j}'
                self.button_dict[name] =  [ Button(window, width = 26, height = 25,
                                    bg = "lightblue", image = self.virtualPixel, borderwidth = 0.5, relief = 'solid',
                                    command = lambda button_info = [name,i,j]: clicked(button_info, self, LayoutProperties)), [i, j]]
                self.button_dict[name][0].grid(row = i+2, column= j)
                self.button_dict[name][0].bind("<Enter>", on_enter)
                self.button_dict[name][0].bind("<Leave>", on_leave)
        

    def new_game(self):
        for i in self.button_dict:
            self.button_dict[i][0].config(state = "normal", bg = "lightblue", image = self.virtualPixel, borderwidth = 0.5, relief = 'solid')
            self.game_matrix = [[0 for i in range(self.column_num)] for j in range(self.row_num)]
            self.clicked_buttons = []
