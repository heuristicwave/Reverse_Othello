def convert_1A_to_ij(corr_str):
    int_i = int(corr_str[0]) - 1

    change = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7
    }

    int_j = change[corr_str[1]]
    return int_i, int_j


def convert_ij_to_1A(i, j):
    str_i = str(i+1)

    change = {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G',
        7: 'H'
    }

    str_j = change[j]
    return str_i + str_j
