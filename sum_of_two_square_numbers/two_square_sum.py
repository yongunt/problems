def squares_sum(n):
    for i in range(31):
        for j in range(31):
            if i**2 + j**2 == n: return True

    return False


print(squares_sum(0)) 
print(squares_sum(1)) 
print(squares_sum(2)) 
print(squares_sum(3)) 
print(squares_sum(5)) 


'''
squares_sum(0) ➞ True
# 0^2 + 0^2 == 0

squares_sum(1) ➞ True
# 0^2 + 1^2 == 1

squares_sum(2) ➞ True
# 1^2 + 1^2 == 2

squares_sum(3) ➞ False
# Checking 0, 1 we can’t make the sum of squares equal to 3.

squares_sum(5) ➞ True
# 1^2 + 2^2 == 5
'''