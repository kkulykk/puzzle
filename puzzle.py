"""
Module to check whether the board satisfies game rules.
https://github.com/kkulykk/puzzle
"""


def check_rule_1(board: list) -> bool:
    """
    Checks whether the board satisfies game rule 1.
    >>> check_rule_1(["**** ****", "***1 ****", "** 3****", "* 4 1****",\
         "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    """
    only_numbers = []
    for i in board:
        number = "".join(j for j in i if j in "0123456789")
        only_numbers.append(number)
        number = ""
    for i in only_numbers:
        if len(i) != len(set(i)):
            return False
    return True


def check_rule_2(board: list) -> bool:
    """
    Checks whether the board satisfies game rule 2.
    >>> check_rule_2(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
         "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    columns = []
    length_of_board = len(board)
    for i in range(length_of_board):
        column = ""
        for k in range(length_of_board):
            column += board[k][i]
        columns.append(column)
    return check_rule_1(columns)


def check_rule_3(board: list) -> bool:
    """
    Checks whether the board satisfies game rule 3.
    >>> check_rule_3(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
         "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> check_rule_3(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
         "     9 5 ", " 6  83  *", "3   1  **", "  6  2***", "  2  ****"])
    False
    """
    board_reversed = board[::-1]
    block = []
    subblock = ""
    for index, i in enumerate(board_reversed):
        for number in i:
            if number in "0123456789":
                subblock += number
                board_reversed[index] = i.replace(number, ' ')
        for k in board_reversed[index+1:]:
            if k[index] in "0123456789":
                subblock += k[index]
                board_reversed[board_reversed.index(
                    k)] = k.replace(k[index], ' ')
        block.append(subblock)
        subblock = ""
    block = [i for i in block if i != '']
    return check_rule_1(block)


def validate_board(board: list) -> bool:
    """
    Check whether the boaard satisfies all the rules.
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
         "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    return check_rule_1(board) and check_rule_2(board) and check_rule_3(board)


doctest.testmod()
