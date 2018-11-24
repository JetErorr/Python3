#8. Even More printing, with a formatter.!
formatter = "{}, {}, {} & {}"

var1 = "one"
var2 = "two"
var3 = "three"

print(formatter.format(var1,var2,var3,"Yellow"))

formatter2 = "{}-{}-{}"

print(formatter2.format(var2,var1,var2))