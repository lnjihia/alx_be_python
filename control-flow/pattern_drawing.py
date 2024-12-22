# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Validate input
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Use a while loop to iterate through rows
    row = 0
    while row < size:
        # Use a for loop to print asterisks in each row
        for _ in range(size):
            print("*", end="")
        # Move to the next line after each row
        print()
        row += 1
