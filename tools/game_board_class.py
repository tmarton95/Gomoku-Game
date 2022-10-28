from tkinter import*
from tools.click_action import clicked

''' Define buttons as the game-board: '''
class GameBoard:
    def __init__(self, layout_properties):
        self.score_p1 = 0
        self.score_p2 = 0
        self.turn = 1
        self.clicked_buttons = []
        self.button_dict = {}
        # Add function for new-game button:
        layout_properties.button_new_game.config(command=lambda: self.new_game(layout_properties))

    # Create game-board with buttons:
    def create_gameboard(self, window, layout_properties):
        row_num, column_num = [layout_properties.row_num, layout_properties.column_num]

        # Cursor-effects:
        def on_enter(e):
            if self.turn < 0:
                e.widget['background'] = 'gray'
            else:
                e.widget['background'] = 'blue'

        def on_leave(e):
            e.widget['background'] = layout_properties.button_color

        # Create zeros matrix:
        self.game_matrix = [[0 for i in range(column_num)] for j in range(row_num)]

        # Create board from buttons:
        for i in range(row_num):
            for j in range(column_num):
                name = f'button_{i}_{j}'
                self.button_dict[name] = [Button(window, 
                                        width=26, 
                                        height=25, 
                                        bg=layout_properties.button_color, 
                                        image=layout_properties.virtualPixel, 
                                        borderwidth=0.5, 
                                        relief='solid',
                                        command=lambda button_info=name: clicked(self, 
                                                                                layout_properties, 
                                                                                button_name=button_info)),
                                        [i, j]]

                self.button_dict[name][0].grid(row=i+2, column=j)
                self.button_dict[name][0].bind("<Enter>", on_enter)
                self.button_dict[name][0].bind("<Leave>", on_leave)

    # Re-generate new game-board:
    def change_board_size(self, window, layout_properties):
        for name in self.button_dict:
            self.button_dict[name][0].destroy()
        self.clicked_buttons = []
        self.button_dict = {}
        self.create_gameboard(window, layout_properties)
        
        width_win, height_win= layout_properties.size_dict[layout_properties.size_current]
        window.geometry(f"{width_win}x{height_win}")

    # Define clear game-board for new game:
    def new_game(self, layout_properties):
        for name in self.button_dict:
            self.button_dict[name][0].config(state="normal", 
                                        bg=layout_properties.button_color, 
                                        image=layout_properties.virtualPixel, 
                                        borderwidth=0.5, 
                                        relief='solid')

        self.game_matrix = [[0 for i in range(layout_properties.column_num)] for j in range(layout_properties.row_num)]
        self.clicked_buttons = []