# Program to add item 7000 after 6000 in the given list
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
index_6000 = list1.index(6000)
list1[index_6000 + 1].append(7000)
print(list1)
