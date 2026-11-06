#!/usr/bin/env python3
def common_elements(set_1, set_2):
    return list(set_1.intersection(set_2)) [:2]

set_1 = {"Python", "Java", "C++"}
set_2 = {"Water", "Python", "Apple"}

print(common_elements(set_1, set_2))
