''' Check game-over: '''
def check_game_over(row_pos, col_pos, mark, game_matrix, row_num, column_num):
    # Initialize data for win-check:
    count_marks_dict = {"count_ver": ["", []],
                        "count_hor": ["", []],
                        "count_cross_up": ["", []],
                        "count_cross_down": ["", []] }

    win_state = False
    win_marks = None
    win_line = 5*mark

    def count_marks(direction, row, col):
        # Check game boundaries:
        if row_num > row >= 0 and column_num > col >= 0:
            count_marks_dict[direction][0] += str(game_matrix[row][col])
            count_marks_dict[direction][1].append([row, col])

    for i in range(-4, 5):
        # Vertical direction:
        count_marks(direction="count_ver",
                    row=row_pos + i,
                    col=col_pos)

        # Horizontal direction:
        count_marks(direction="count_hor",
                    row=row_pos,
                    col=col_pos + i)

        # Cross-Up direction:
        count_marks(direction="count_cross_up",
                    row=row_pos - i,
                    col=col_pos + i)

        # Cross-Down direction:
        count_marks(direction="count_cross_down",
                    row=row_pos + i,
                    col=col_pos + i)

    for value in count_marks_dict.values():
        if win_line in value[0]:
            win_state = True
            mark_start = value[0].index(win_line)
            win_marks = value[1][mark_start:mark_start+5]
            win_marks.append([row_pos, col_pos])
            break

    return win_state, win_marks