from tkinter import*
from tools import game_board_class, layout_class
from tools.other_functions import reset_scores, open_settings

# Initial properties:
row_num = 20
column_num = 20
score_p1 = 0
score_p2 = 0

if __name__ == '__main__':
    window = Tk()
    window.title("Gomoku")
    window.geometry('600x650')
    window.call('wm', 'iconphoto', window._w, PhotoImage(file = 'icons\\icon_app.png'))

    # Define Layout, labels:
    LayoutProperties = layout_class.Layout(window)

    # Define board of game:
    BoardProperties = game_board_class.GameBoard(window, LayoutProperties)

    # Define Menu-bar:
    menu = Menu(window)
    new_item = Menu(menu, tearoff = 0)
    new_item.add_command(label='Reset Scores', command = lambda: reset_scores(BoardProperties, LayoutProperties))
    new_item.add_separator()
    new_item.add_command(label = 'Settings', command = lambda: open_settings(window))
    menu.add_cascade(label = 'File', menu = new_item)
    window.config(menu = menu)
    #=====================================
    window.mainloop()