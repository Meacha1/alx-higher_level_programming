#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(0, x):
            if i+1 == x:
                print("{:d}".format(my_list[i]))
                count += 1
            else:
                print("{:d}".format(my_list[i]), end = "")
                count += 1
    except:
        print()
    return count
