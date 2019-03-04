#%%
print("Hello world.!")

#%%
a = 1
print(type(a))
print(a, "is the answer")

#%%
a = 5
b = 7
c = 1
if a > b:
    if a > c:
        print("A is greater")
        print("In 2nd if")
    else:
        print("C is greater")
else:
    if b > c:
        print("B is greater")
        print("in 1st if")

#%%
print("Hello")

#%%
a = input("Enter your age:")
a = int(a)
if a < 20:
    print("Youngster")
elif a <= 20 and a <= 45:
    print("Adult")
else:
    print("Old")

#%%
#list
fav = []
print(fav)
fav.append("Hii")
print(fav)

fav2 = ["hii", 10, 20.4]
print(fav2)
del fav2[0]
print(fav2)
print(type(fav2))

#%%
fav = {}
fav['color']='Red'
print(fav)
fav.update({
    'subject': 'Machine Learning',
    'Marks': [10,20],
})
print(fav)
fav[10]="ml_marks"
del fav['color']
print(fav['subject'])
print(fav)
print(type(fav))


#%%
# a [include : exclude
a = [1,2,3,4,5,7,8,9]
print(len(a))
print(a[:])
print(a[:5])
print(a[:-1])
print(a[-1:])

#%%
a = [1,2,3,4,5,7,8,9]
for i in a:
    print(i)

#%%
for i in range(4):
    print(i)
print('***************************')
for i in range(0,10000):
    print(i)

#%%
def set_x(num):
    x = num
    print(x)
    return x

y=43
z=set_x(y)
print("Z is",z)

#%%
a = 4.5
b = 15.0
c = a + b
print("The sum of ",a,"and ",b,"is ",c)


#%%
a = 23546576
# b = 27
flag = 0
for i in range(2,(a-1)):
    if (a%i == 0):
        # print(i)
        flag = 1

if (flag == 1):
    print("Number not prime.!")
else:
    print("Number is prime.!")


#%%
def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)
print("5 fact")
print(fact(5))
