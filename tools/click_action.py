from tkinter import messagebox
from tools import win_checks

''' Update gameboard after the click + start win-check:'''
def clicked(board_properties, layout_properties, button_name):
    # Update table + turn:
    if button_name not in board_properties.clicked_buttons:
        row_pos, col_pos = board_properties.button_dict[button_name][1]
        if board_properties.turn < 0:
            mark = "x"
            board_properties.button_dict[button_name][0].config(image = layout_properties.x_icon)
            board_properties.game_matrix[row_pos][col_pos] = mark
            layout_properties.label_turn.config(text = "Player 2 turn:")
            layout_properties.label_turn_image.config(image = layout_properties.o_icon)
            
        elif board_properties.turn > 0:
            mark = "o"
            board_properties.button_dict[button_name][0].config(image = layout_properties.o_icon)
            board_properties.game_matrix[row_pos][col_pos] = mark
            layout_properties.label_turn.config(text = "Player 1 turn:")
            layout_properties.label_turn_image.config(image = layout_properties.x_icon)

        board_properties.clicked_buttons.append(button_name)
        board_properties.turn *= -1

        # Check end of game:
        win_status, win_marks = win_checks.check_game_over(row_pos, 
                                                            col_pos, 
                                                            mark, 
                                                            game_matrix = board_properties.game_matrix,
                                                            row_num = layout_properties.row_num,
                                                            column_num = layout_properties.row_num)
        if win_status:
            # de-activate buttons:
            for button_name in board_properties.button_dict:
                board_properties.button_dict[button_name][0].config(state = "disabled")

            # Get red color for winner:
            find_winners(board_properties, layout_properties, win_marks, mark)

            # Update scores:
            if mark == "x":
                play_num = 1
                board_properties.score_p1 += 1
                layout_properties.label_p1_score.config(text = str(board_properties.score_p1))
            elif mark == "o":
                play_num = 2
                board_properties.score_p2 += 1
                layout_properties.label_p2_score.config(text = str(board_properties.score_p2))

            messagebox.showinfo(title="GAME OVER", message = f"Player {play_num} win!")

''' Collect and highlight the winner-marks:'''
def find_winners(board_properties, layout_properties, win_marks, mark):
    if mark == "x":
        red_icon = layout_properties.x_icon_red
    elif mark == "o":
        red_icon = layout_properties.o_icon_red

    for button_name in board_properties.button_dict:
        for win_coord in win_marks:
            row_pos, col_pos= board_properties.button_dict[button_name][1]
            if [row_pos, col_pos] == win_coord:
                board_properties.button_dict[button_name][0].config(image = red_icon)
