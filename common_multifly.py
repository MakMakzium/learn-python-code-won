'''
An integer number and n,m are given.
If the number is a multiple of n and a multiple of m, complete the solution function to return 0 if it is not 1
'''

def solution(n : int , m : int , number) -> int :
    if  number % (n*m) == 0:
        return 1
    else :
        return 0
    
n=3
m=2
number= int(input("please input number (multiple of n and m)"))
sol = solution(3,2,number)
print(sol)