from tkinter import*
    
''' Reset scores: '''
def reset_scores(board_properties, layout_properties):
    board_properties.score_p1 = 0
    board_properties.score_p2 = 0
    layout_properties.label_p1_score.config(text = "0")
    layout_properties.label_p2_score.config(text = "0")

''' Open settings-window: '''
def open_settings(window, board_properties, layout_properties, images_folder):
    WIDTH_win = 250
    HEIGHT_win = 200
    HEIGHT_button = 40
    COLOR_bg = "#eddb90"
    win_setting = Toplevel(window, height = HEIGHT_win - 4, width = WIDTH_win+5)
    win_setting.grab_set()
    win_setting.title("Settings")
    window.call('wm', 'iconphoto', win_setting._w, PhotoImage(file = images_folder + '\\icon_settings.png'))

    canvas_colors = Canvas(win_setting, 
                            height = HEIGHT_win - HEIGHT_button, 
                            width = WIDTH_win/2, 
                            bg = COLOR_bg, 
                            relief = 'ridge', 
                            borderwidth = 1)
    canvas_colors.place(x = 0, y = 0)

    canvas_size = Canvas(win_setting, 
                            height = HEIGHT_win - HEIGHT_button, 
                            width = WIDTH_win/2, 
                            bg = COLOR_bg, 
                            relief = 'ridge', 
                            borderwidth = 1)
    canvas_size.place(x = WIDTH_win/2, y = 0)

    label_color = Label(canvas_colors, 
                            text = 'Appearance', 
                            font = ('Verdana', 9),
                            relief = 'ridge',
                            borderwidth=1,
                            bg = COLOR_bg,
                            width = 15,
                            height = 2)
    label_color.place(x = 4, y = 0)

    label_size = Label(canvas_size, 
                            text = 'Board size', 
                            font = ('Verdana', 9),
                            relief = 'ridge',
                            borderwidth = 1,
                            bg = COLOR_bg,
                            width = 15,
                            height = 2)
    label_size.place(x = 4, y = 0)

    # Variables for radio-buttons:
    v_color = StringVar()
    v_color.set(layout_properties.style_current)

    v_size = IntVar()
    v_size.set(layout_properties.size_current)

    # Color options:
    color_button_normal = Radiobutton(canvas_colors, 
                                        text = 'Normal style', 
                                        variable = v_color, 
                                        value = 'normal',
                                        background = COLOR_bg)
    color_button_normal.place(x = 5, y = 50)

    color_button_dark = Radiobutton(canvas_colors, 
                                        text = 'Dark style', 
                                        variable = v_color, 
                                        value = 'dark',
                                        background = COLOR_bg)
    color_button_dark.place(x = 5, y = 100)

    # Size options:
    size_button_small = Radiobutton(canvas_size, 
                                        text = '10 x 10', 
                                        variable = v_size, 
                                        value = 10, 
                                        background = COLOR_bg)                            
    size_button_small.place(x = 15, y = 40)

    size_button_middle = Radiobutton(canvas_size, 
                                        text = '15 x 15', 
                                        variable = v_size, 
                                        value = 15, 
                                        background = COLOR_bg)
    size_button_middle.place(x = 15, y = 80)

    size_button_middle = Radiobutton(canvas_size, 
                                        text = '20 x 20', 
                                        variable = v_size, 
                                        value = 20, 
                                        background = COLOR_bg)
    size_button_middle.place(x = 15, y = 120)

    # Apply props.:
    button_apply = Button(win_setting, 
                text = 'Apply settings', 
                font = ('Helvetica', 10, 'italic'), 
                width = 30, 
                bg = 'lightgreen',
                command = lambda: apply_properties(window, board_properties, layout_properties, v_color, v_size))

    button_apply.place(x = 3, y = HEIGHT_win - HEIGHT_button + 6)

''' Apply settings: (and reset game!) '''
def apply_properties(window, board_properties, layout_properties, v_color, v_size):
    layout_properties.style_current = v_color.get()
    layout_properties.size_current = v_size.get()
    layout_properties.change_style()
    layout_properties.create_label_board()
    board_properties.change_board_size(window, layout_properties)