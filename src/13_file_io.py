"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

f = open('foo.txt')
print(f.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

f2 = open('bar.txt', 'w')
f2.write('Line 1 \n')
f2.write('Line 2 \n')
f2.write('Line 3 \n')
f2.close()

f2_check = open('bar.txt')
print(f2_check.read())