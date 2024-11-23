# pip install hashlib

import hashlib as hh

def calculate_love_percentage(name1, name2):
    combined_names = ''.join(sorted([name1.lower(), name2.lower()]))
    hash_object = hh.md5(combined_names.encode())
    hash_hex = hash_object.hexdigest()
    hash_int = int(hash_hex, 16)
    percentage = (hash_int % 100) + 1
    return percentage
def main():
    print("Welcome to the Love Calculator!")
    name1 = input("Enter the boy name: ").strip()
    name2 = input("Enter the girl name: ").strip()
    if not name1 or not name2:
        print("Both names must be provided.")
        return
    percentage = calculate_love_percentage(name1, name2)
    print(f"The love percentage between {name1} and {name2} is: {percentage}%")

if __name__ == "__main__":
    main()
