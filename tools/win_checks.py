'''
Check game-over:
'''
def check_game_over(row_pos, col_pos, mark, game_matrix, row_num, column_num):
    count_marks = {"count_ver": [1, []], "count_hor": [1, []],
                    "count_cross_up": [1, []], "count_cross_down": [1, []]}

    for i in range(4):
        '''
        Check vertical direction:
        '''
        # + direction
        row = row_pos + i + 1
        col = col_pos
        if (row_num > row >= 0 and column_num > col >= 0) and game_matrix[row][col] == mark:
            count_marks["count_ver"][0] += 1
            count_marks["count_ver"][1].append([row, col])

        # - direction:
        row = row_pos - (i+1)
        col = col_pos
        if (row_num > row >= 0 and column_num > col >= 0) and game_matrix[row][col] == mark:
            count_marks["count_ver"][0] += 1
            count_marks["count_ver"][1].append([row, col])
        '''
        Check horizontal direction:
        '''
        # + direction
        row = row_pos
        col = col_pos + i + 1
        if row_num > row >= 0 and column_num > col >= 0 and game_matrix[row][col] == mark:
            count_marks["count_hor"][0] += 1
            count_marks["count_hor"][1].append([row, col])

        # - direction:
        row = row_pos
        col = col_pos - (i+1)
        if row_num > row >= 0 and column_num > col >= 0 and game_matrix[row][col] == mark:
            count_marks["count_hor"][0] += 1
            count_marks["count_hor"][1].append([row, col])
        '''
        Check cross-up direction:
        '''
        # + direction:
        row = row_pos - (i+1)
        col = col_pos + i + 1
        if row_num > row >= 0 and column_num > col >= 0 and game_matrix[row][col] == mark:
            count_marks["count_cross_up"][0] += 1
            count_marks["count_cross_up"][1].append([row, col])

        # - direction:
        row = row_pos + i + 1
        col = col_pos - (i+1)
        if row_num > row >= 0 and column_num > col >= 0 and game_matrix[row][col] == mark:
            count_marks["count_cross_up"][0] += 1
            count_marks["count_cross_up"][1].append([row, col])
        '''
        Check cross-down direction:
        '''
        # + direction:
        row = row_pos + i + 1
        col = col_pos + i + 1
        if row_num > row >= 0 and column_num > col >= 0 and game_matrix[row][col] == mark:
            count_marks["count_cross_down"][0] += 1
            count_marks["count_cross_down"][1].append([row, col])

        # - direction:
        row = row_pos - (i+1)
        col = col_pos - (i+1)
        if row_num > row >= 0 and column_num > col >= 0 and game_matrix[row][col] == mark:
            count_marks["count_cross_down"][0] += 1
            count_marks["count_cross_down"][1].append([row, col])

    win_state = False
    win_marks = None
    for key in count_marks:
        if count_marks[key][0] >= 5:
            win_state = True
            win_marks = count_marks[key][1]
            win_marks.append([row_pos, col_pos])
            break

    return win_state, win_marks