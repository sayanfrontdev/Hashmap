from ast import Num


def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
num=int(input("Enter the number :\n"))
print(f"Sum of {num} is", sum(num))    
