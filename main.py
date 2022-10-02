from tkinter import*
from tools import game_board_class, layout_class

window = Tk()
window.title("Gomoku")
window.geometry('600x650')

window.call('wm', 'iconphoto', window._w, PhotoImage(file = 'icons\\icon_app.png'))

# Initial properties:
row_num = 20
column_num = 20
score_p1 = 0
score_p2 = 0

# Define Layout / Appearance:
LayoutProperties = layout_class.Layout(window)

# Define board of game:
BoardProperties = game_board_class.GameBoard(window, row_num, column_num, score_p1, score_p2, LayoutProperties)

# Define button for new game:
button_new_game = Button(window, text = "New Game", font = ('Helvetia', 10), background="orange",
                                        height = 2, width = 16, command = BoardProperties.new_game)
button_new_game.grid(row = 0, column = 14, columnspan = 18, rowspan=2, sticky='e')
#=====================================
# Additional functions:
def reset_scores():
    BoardProperties.score_p1 = 0
    BoardProperties.score_p2 = 0
    LayoutProperties.label_p1_score.config(text = "0")
    LayoutProperties.label_p2_score.config(text = "0")

def settings():
    win_setting = Toplevel()
    win_setting.title = "Settings"
    win_setting.geometry = ('200x200')
    Label(win_setting, text = "Settings...").pack()

#=======================================
menu = Menu(window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Reset Scores', command = reset_scores)
new_item.add_separator()
new_item.add_command(label='Settings', command = settings)
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)
#=====================================
window.mainloop()