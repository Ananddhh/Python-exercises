def is_substring_present(main_string, substring):
    return substring in main_string

main_string = input("Enter the main string: ")
substring = input("Enter the substring to search for: ")

if is_substring_present(main_string, substring):
    print("Yes, the substring is present in the main string.")
else:
    print("No, the substring is not present in the main string.")

