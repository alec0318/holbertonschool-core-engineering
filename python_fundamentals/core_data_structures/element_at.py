#!/usr/bin/env python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    else:
        return my_list[idx]


my_list = [1, 2, 3]

print("Element at index 1 is {}".format(element_at(my_list, 1)))
