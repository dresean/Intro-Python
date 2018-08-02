import os
# Use open to open file "foo.txt" for reading
def open_foo():
  foo = open('foo.txt', 'r')
  for line in foo:
    print(line)
  foo.close()
  print('foo closed')
# Print all the lines in the file

# Close the file
open_foo()

# Use open to open file "bar.txt" for writing
def open_file():
  name = input("Enter a file name, don't forget the . extension : ")
  file = open('{}'.format(str(name)), 'w+')
  num = input('Enter the number of lines to write: ')
  for i in range(int(num)):
    lines = input('Enter the lines here: ')
    file.write(f'{lines} \n')
    print('Line written! ')
  file.close()
  print('File closed! ')

open_file()
# Use the write() method to write three lines to the file

# Close the file