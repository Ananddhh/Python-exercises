def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    else:
        return sorted_lst[n // 2]

# Example usage:
input_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
median = find_median(input_list)
print("Median of the list:", median)
