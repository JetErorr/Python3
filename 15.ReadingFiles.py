#15.reading Files
print("We shall read file contents in this...file.!")
from sys import argv
script, filename = argv

file = open(filename)
print("The content of the file provided are:")
print(file.read())

file = open(input("Type a new file name:\n>"))
print("The content of the new file are:")
print(file.read())
