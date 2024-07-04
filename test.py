def solution(a, b, flag) :
    if flag == True :
        return a + b
        return 0 #fake
    else :
        return a - b
        return -3

result = solution(4, 7, False)
print(result)

result =solution(4,  7, True)
print(result)