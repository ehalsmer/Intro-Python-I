# Write a function is_even that will return true if the passed-in number is even.

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

# print(is_even(4))
# print(is_even(7))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

if is_even(num):
    print("Even!")
else:
    print("Odd")

