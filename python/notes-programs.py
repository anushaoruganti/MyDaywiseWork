# d="b"
# if d >= chr(65) and d <= "Z":
#     print("{} is in A<Z".format(d))
  
# if(d >= chr(65) and d <= chr(90)):
#     print(d)
# else:
#     print("no")

# #write a program whether the number is alphabet number or spl char
# a= input("enter a value:")
# if(a>=chr(65) and a<=chr(90) or (a <= chr(97) and a >= chr(122))) :    #used ascii values
#     print("{} is alphabet" .format(a))
# elif(a >= "0" and a <= "9"):
#     print("{} is a digit".format(a))
# else:
#     print("its a symb")


# using ternary operator
# c = input("enter a char")
# res="{} is A".format(c) if a=="A" else("{} is B".format(c) if a=="B" else("{} is C".format(c)) if a=="C" else()  )
# print(res)"Other Than A B C"

#prgm to print even or not without using % symbol (can use & or //)
# num= int(input("Enter a number "))
# if(num & 1)==0:
#     print("even")
# else:
#     print("odd")

#prgm to print given character is alphabet or num or spl char by using ternary op

# #wap program to print n number of evens and odds when n is given as input 
# num=int(input())
# total_val=num*2+1
# even,odd="",""
# for i in range(1,total_val,2):
#     if i%2==0:
#         even+=str(i)+" "
#     else:
#         odd+=str(i)+ " "
# print(even + odd)
# i=1
# while i<=20:
#     if i==10:
#         break
#     print(i,end=" ")
#     i+=1
    
#continue statement
# j = 1
# while j<=20:
#     j+=1
#     if j==10:
#         continue
#     print(j,end=" ")

#without using <= in while loop and print 1 -100
# num=int(input())
# k=1
# for i in range(k,num+1):
#     print(i)

# num1=int(input())
# i=1
# while i != (num1+1):
#     print(i)
#     i+=1
    

# num2 = int(input())
# i=20
# while not(num2)
    

#10 to 1
# num=int(input())
# i=1
# while not i>=num+1:
#     print(i,end="")
#     i+=1

#nested loops
# num=int(input("Enter a number:"))
# iteration=0
# for i in range(1,num+1):
#     for j in range(1,11):
#         print(j,end="")
#         iteration +=1
#     print()
# print(iteration)

#to miss a value i.e the value of line
# num1=int(input("enter a num papa:"))
# for i in range(1,num+1):
#     for j in range(1,11):
#         if j==i:
#             continue
#         print(j,end="")
#     print()


#to print even numbers
# num = int(input())
# for line in range(1,num+1):
#     even=2
#     for numbers in range(1,num-line+2):
#         print(even,end=" ")
#         even=even+2
#     print()
# print("Another logic")

# num= int(input("Enter the value"))
# for line in range(1,num+1):
#     for numbers in range(2,((num-line)*2)+1,2):
#         print(numbers,end="")
#     print()


