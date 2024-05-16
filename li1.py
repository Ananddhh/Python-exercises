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

# Finding the Range of a List of Numbers

# Create a list of numbers
num_list = [10, 5, 20, 15, 8]

# Find the range (difference between the largest and smallest element)
range_of_list = max(num_list) - min(num_list)

# Print the range
print("Range of the list:", range_of_list)


# Counting the Frequency of Elements in a List of Random Numbers

from collections import Counter
import random

# Create a list of random numbers
random_list = [random.randint(1, 10) for _ in range(20)]

# Count the frequency of each element
element_count = Counter(random_list)

# Print the frequency of each element
for element, count in element_count.items():
    print(f"Element {element} appears {count} times.")


#  Inserting an Element at a Specific Position in a List of Numbers

# Create a list of numbers
num_list = [10, 20, 30, 40, 50]

# Insert a new element (e.g., 25) at a specific position (e.g., index 2)
new_element = 25
position = 2
num_list.insert(position, new_element)

# Print the updated list
print("Updated list after insertion:", num_list)
