# Program to add item 7000 after 6000 in the given list
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
index_6000 = list1.index(6000)
list1[index_6000 + 1].append(7000)
print(list1)

# Program to find value 20 in the list, and if it is present, replace it with 200
list1 = [5, 10, 15, 20, 25, 50, 20]
index_20 = list1.index(20)
list1[index_20] = 200
print(list1)


# Program to find the range (difference between the largest and smallest element) of a list of numbers
numbers = [10, 5, 20, 15, 25]
range_of_numbers = max(numbers) - min(numbers)
print("Range of the list:", range_of_numbers)
