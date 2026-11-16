#!/usr/bin/env python3

"""class VerboseList"""


class VerboseList(list):

    """append method"""
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    """extend method"""
    def extend(self, item):
        super().extend(item)
        print(f"Extended the list with {len(item)} items.")

    """remove method"""
    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    """pop method"""
    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)


vl = VerboseList([1, 2, 3])

vl.append(4)
vl.extend([5, 6])
vl.remove(2)
vl.pop(0)
