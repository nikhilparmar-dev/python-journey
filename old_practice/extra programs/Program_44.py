# Write a Python program to insertion at the beginning in OrderedDict.
# Date : 07/03/2026
# Author : Nikhil


from collections import OrderedDict

ordered_dict = OrderedDict([('b', 2), ('c', 3), ('d', 4)])

new_item = ('a', 1)

new_orderd_dict = OrderedDict([new_item])

new_orderd_dict.update(ordered_dict)


print("Updated OrderedDict:", new_orderd_dict)