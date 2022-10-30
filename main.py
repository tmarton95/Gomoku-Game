from tkinter import*
from tools import layout_class
from tools import game_board_class
from tools.options import reset_scores, open_settings

images_folder = 'icons'

def run_game():
    window = Tk()
    window.title("Gomoku")
    window.geometry('600x650')
    window.call('wm', 'iconphoto', window._w, PhotoImage(file = images_folder + '\\icon_app.png'))

    # Define Layout, labels:
    layout_properties = layout_class.Layout(window, images_folder)
    layout_properties.create_label_board()

    # Define board of game:
    board_properties = game_board_class.GameBoard(layout_properties)
    board_properties.create_gameboard(window, layout_properties)

    # Define Menu-bar:
    menu = Menu(window)
    new_item = Menu(menu, tearoff = 0)
    new_item.add_command(label='Reset Scores', 
                        command = lambda: reset_scores(board_properties, layout_properties))
    new_item.add_separator()
    new_item.add_command(label = 'Settings', 
                        command = lambda: open_settings(window, board_properties, layout_properties, images_folder))
    menu.add_cascade(label = 'File', menu = new_item)
    window.config(menu = menu)
    #----------------
    window.mainloop()

if __name__ == '__main__':
    run_game()