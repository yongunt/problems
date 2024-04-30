def multiplication_table(n:int) -> list:
    ans:list = []
    holder:list = []

    for i in range(1, n+1):
        for j in range(1, n+1):
            holder.append(i*j)
        
        ans.append(holder)
        holder = []

    return ans


print(multiplication_table(1))
print(multiplication_table(3))


'''
multiplication_table(1) ➞ [[1]]

multiplication_table(3) ➞ [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
'''