# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard


def is_even():
  num = input("Enter a number: ")
  if int(num) % 2 == 0:
    print('Even!')
  else:
    print('Odd')

is_even()
# Print out "Even!" if the number is even. Otherwise print "Odd"