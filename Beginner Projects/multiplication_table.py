# Code Created By @Dypixx....

number = int(input("Enter the number for which you want the multiplication table: "))

# Display the multiplication table
print(f"Multiplication Table for {number}:")
for i in range(1, 11):  # Loop through numbers from 1 to 10
    print(f"{number} x {i} = {number * i}")  # Display Output

