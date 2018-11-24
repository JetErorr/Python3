#13.Parameters, Unpacking and Variables
from sys import argv
print("Hey, you see that import line above? That will add a new module to this file and you will be able to use the functionality of those modules into whatever files you import them into.")
print("The use of modules will reduce the repeatition of code across similar files.")

arg1, arg2, arg3, arg4 = argv

print("The first argument, which is the actual filename, passed form the terminal is:",arg1)
print("The second argument passed from the termial is:",arg2)
print("The third argument passed from the terminal is:",arg3)
print("The fourth argument passed from the terminal is:",arg4)