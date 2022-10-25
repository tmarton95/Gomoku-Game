from tkinter import messagebox
from tools import win_checks

''' Update gameboard after the click + start win-check:'''
def clicked(BoardProperties, LayoutProperties, button_name):
    # Update table + turn:
    if button_name not in BoardProperties.clicked_buttons:
        row_pos, col_pos = BoardProperties.button_dict[button_name][1]
        if BoardProperties.turn < 0:
            mark = "x"
            BoardProperties.button_dict[button_name][0].config(image = LayoutProperties.x_icon)
            BoardProperties.game_matrix[row_pos][col_pos] = mark
            LayoutProperties.label_turn.config(text = "Player 2 turn:")
            LayoutProperties.label_turn_image.config(image = LayoutProperties.o_icon)
            
        elif BoardProperties.turn > 0:
            mark = "o"
            BoardProperties.button_dict[button_name][0].config(image = LayoutProperties.o_icon)
            BoardProperties.game_matrix[row_pos][col_pos] = mark
            LayoutProperties.label_turn.config(text = "Player 1 turn:")
            LayoutProperties.label_turn_image.config(image = LayoutProperties.x_icon)

        BoardProperties.clicked_buttons.append(button_name)
        BoardProperties.turn *= -1

        # Check end of game:
        win_status, win_marks = win_checks.check_game_over(row_pos, 
                                                            col_pos, 
                                                            mark, 
                                                            game_matrix = BoardProperties.game_matrix,
                                                            row_num = LayoutProperties.row_num,
                                                            column_num = LayoutProperties.row_num)
        if win_status:
            # de-activate buttons:
            for button_name in BoardProperties.button_dict:
                BoardProperties.button_dict[button_name][0].config(state = "disabled")

            # Get red color for winner:
            find_winners(BoardProperties, LayoutProperties, win_marks, mark)

            # Update scores:
            if mark == "x":
                play_num = 1
                BoardProperties.score_p1 += 1
                LayoutProperties.label_p1_score.config(text = str(BoardProperties.score_p1))
            elif mark == "o":
                play_num = 2
                BoardProperties.score_p2 += 1
                LayoutProperties.label_p2_score.config(text = str(BoardProperties.score_p2))

            messagebox.showinfo(title="GAME OVER", message = f"Player {play_num} win!")

''' Collect and highlight the winner-marks:'''
def find_winners(BoardProperties, LayoutProperties, win_marks, mark):
    if mark == "x":
        red_icon = LayoutProperties.x_icon_red
    elif mark == "o":
        red_icon = LayoutProperties.o_icon_red

    for button_name in BoardProperties.button_dict:
        for win_coord in win_marks:
            row_pos, col_pos= BoardProperties.button_dict[button_name][1]
            if [row_pos, col_pos] == win_coord:
                BoardProperties.button_dict[button_name][0].config(image = red_icon)
