#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(0, len(my_list), 1):
        if i == idx:
            return(my_list[i])
    if idx < 0:
        return (None)
    if idx > (len(my_list) - 1):
        return (None)
