from tkinter import*

class Layout:
    def __init__(self, window, images_folder):
        ''' Images + initial style: '''
        # Pictures for marks:
        x_icon_normal = PhotoImage(file=images_folder + '\\x_icon.png')
        o_icon_normal = PhotoImage(file=images_folder + '\\o_icon.png')
        x_icon_dark = PhotoImage(file=images_folder + '\\x_icon_dark.png')
        o_icon_dark= PhotoImage(file=images_folder + '\\o_icon_dark.png')
        # Winner indicators:
        self.x_icon_red = PhotoImage(file=images_folder + '\\x_icon_red.png')
        self.o_icon_red= PhotoImage(file=images_folder + '\\o_icon_red.png')

        virtualPixel_normal = PhotoImage(file=images_folder + '\\virtual_pix.png')
        virtualPixel_dark = PhotoImage(file=images_folder + '\\virtual_pix_dark.png')
        
        # Initial board-style:
        self.size_current = 20
        self.row_num = self.column_num = self.size_current
        self.size_dict = {10: ['300', '340'],
                        15: ['450', '485'],
                        20: ['600', '630']}

        self.style_current = 'normal'
        self.style_dict = {'normal': ['lightblue', x_icon_normal, o_icon_normal, virtualPixel_normal],
                            'dark': ['darkblue', x_icon_dark, o_icon_dark, virtualPixel_dark]}

        [self.button_color, 
        self.x_icon, 
        self.o_icon, 
        self.virtualPixel] = self.style_dict[self.style_current][0:4]

        self.button_pos = {10: {'column': 5, 'width': 12},
                        15: {},
                        20: {'column': 14, 'width': 16}}

        ''' Labels + button on board: '''
        self.label_score = Label(window, text='Scores:', font=('Verdana', 12), pady=10)
        self.label_p1 = Label(window, text='Player 1:', font=('Verdana', 10, 'bold'))
        self.label_p2 = Label(window, text='Player 2:', font=('Verdana', 10, 'bold'))
        self.label_p1_score = Label(window, text='0', font=('Verdana', 14, 'bold'))
        self.label_p2_score = Label(window, text='0', font=('Verdana', 14, 'bold'))
        self.label_turn = Label(window, text='Player 1 turn:', font=('Verdana', 10,))
        self.label_turn_image = Label(window, image = self.x_icon)

        self.button_new_game = Button(window, 
                                    text="New Game", 
                                    font=('Helvetia', 10), 
                                    background="orange",
                                    height=2, 
                                    width=self.button_pos[self.size_current]['width'])

        self.button_new_game.grid(row=0, 
                                column=self.button_pos[self.size_current]['column'], 
                                columnspan=18, 
                                rowspan=2, 
                                sticky='e')

    def create_label_board(self):
        self.button_new_game.config(width=self.button_pos[self.size_current]['width'])
        self.button_new_game.grid(row=0, 
                                column=self.button_pos[self.size_current]['column'])
        if self.size_current == 10:
            self.label_score.grid_forget()
            self.label_p1.grid(row=0, column=0, sticky='w')
            self.label_p2.grid(row=0, column=3, sticky='w')
            self.label_p1_score.grid(row=1, column=0, sticky='w', padx=22)
            self.label_p2_score.grid(row=1, column=3, sticky='w', padx=22)
            self.label_turn.grid_forget()
            self.label_turn_image.grid_forget()
            
        elif self.size_current == 15:
            pass
        
        elif self.size_current == 20:
            # Arrange normally labels+button:
            self.label_score.grid(row=0, column=0, columnspan=18, rowspan=2, sticky='w')
            self.label_p1.grid(row=0, column=3, columnspan=18, sticky='w')
            self.label_p2.grid(row=0, column=6, columnspan=18, sticky='w')
            self.label_p1_score.grid(row=1, column=3, columnspan=18, sticky='w', padx=22)
            self.label_p2_score.grid(row=1, column=6, columnspan=18, sticky='w', padx=22)
            self.label_turn.grid(row=0, column=8, columnspan=18, rowspan=2, sticky='w', padx=22)
            self.label_turn_image.grid(row=0, column=11, columnspan=18, rowspan=2, sticky='w', padx=33)
            
    
    def change_style(self):
        [self.button_color, 
        self.x_icon, 
        self.o_icon, 
        self.virtualPixel] = self.style_dict[self.style_current][0:4]
        self.row_num = self.column_num = self.size_current
        
        