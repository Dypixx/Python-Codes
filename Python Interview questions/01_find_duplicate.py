# Q1. Write a Python function that takes a list of integers as input and returns all duplicate numbers found in the list.

def find_all_duplicates(nums):
    seen = set()
    duplicates = set()
    for i in nums:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)
    return list(duplicates)


nums = [1, 2, 3, 4, 5, 2]
print("===================")
print("Solved By @Dypixx")
print("===================")
print()
print("Duplicate numbers:", find_all_duplicates(nums))
print()
