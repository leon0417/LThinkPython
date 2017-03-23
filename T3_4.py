from T3_3 import *

def print_large_table():

    for i in range(4):
        for j in range(4):
            print_row()
        print_lst_corner()
        for j in range(4):
            for k in range(4):
                print_cow()
            print_lst_cow()


    for i in range(4):
        print_row()
    print_lst_corner()