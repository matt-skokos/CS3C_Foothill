""" Some practice writing recurrence relation. """

def pascal_number(row, column):
    """Return the number in a specific row / column """
    if row == 0:
        return 1
    else:
        return pascal_number(row-1, column) + pascal_number(row-1, column -1)

print(pascal_number(0,1))
print(pascal_number(1, 3))


def pascal_line(n):
    """ Return nth line of pascal's trinagle. """
    line_list = []
    if n == 0:
        return 1
    else:
        return pascal_line(n -1) + n

print(pascal_line(1))