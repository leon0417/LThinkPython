from T3_2 import *
def print_row():
    print('+ ', '- ' * 4, end=' ')
def print_lst_corner():
    print('+')


def print_cow():
    print('| ', ' ' * 8, end=' ')
def print_lst_cow():
    print('|')

def print_table():
    run_twice(print_row)
    print_lst_corner()

    run_twice(print_cow)
    print_lst_cow()
    run_twice(print_cow)
    print_lst_cow()
    run_twice(print_cow)
    print_lst_cow()
    run_twice(print_cow)
    print_lst_cow()

    run_twice(print_row)
    print_lst_corner()

    run_twice(print_cow)
    print_lst_cow()
    run_twice(print_cow)
    print_lst_cow()
    run_twice(print_cow)
    print_lst_cow()
    run_twice(print_cow)
    print_lst_cow()

    run_twice(print_row)
    print_lst_corner()

    # for i in range(2):
    #     for j in range(2):
    #         print_row()
    #     print_lst_corner()
    #     for j in range(4):
    #         for k in range(2):
    #             print_cow()
    #         print_lst_cow()
    #
    #
    # for i in range(2):
    #     print_row()
    # print_lst_corner()