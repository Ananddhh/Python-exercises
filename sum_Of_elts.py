input_list = list(map(int, input("Enter numbers separated by commas:").split(',')))
sum = 0
for num in input_list:
    sum += num
print("sum is ", sum)
