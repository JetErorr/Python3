#Strings and Texts
print("5.Strings and Texts.!")
print("Strings are nothing but characters, just a set of them used together")
print("Strings are enclosed in double quotes (\"\") or sometimes with single quotes (\'\')")
print("Now you already are working with strings with the past 4 files,")
print("So, we will go a little further with this file.!")
#String Formatting
a = "String One"
b = "String Two"
x = "This string will have the combination of both the strings above. a: {} and b: {}"
#This is a quite similar to the way we used to embed variables in strings before in file 4.
print(x.format(a,b))
print("And we can combine strings as well. Append is the word here.")
aa = "Left Side + "
bb = "Right Side"
print(aa + bb)
#OK, lastly.
var = False
var0 = "Can we end this file now.? {}"
print(var0.format(var))
var = True
print(var0.format(var))
#Those were boolean variables: var and var0