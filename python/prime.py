a=int(input())
if(a%2==0 & a>2):
    print("{} is not prime ".format(a))
elif(a==2):
    print("2 is prime number")

else:
    print("{} is prime number".format(a))


if(a%2==0):
    print("get lost")
else:
    array = list(map(int, str(a)))
    print(array)

num=6
print(~num)

print(10 or 2)

print(10 or 5 or 6)
print(5 or 10 or 3)

c=8
b=2
a=c|b

print(a)

