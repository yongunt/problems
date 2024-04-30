def floyd(up_to = None, n_row = None):
    triangle = []
    holder = []
    a = 1


    if n_row != None:
        for i in range(1, n_row + 1):
            while i > len(holder):
                holder.append(a)
                a += 1
            triangle.append(holder)
            holder = []

        return triangle
    
    else:
        check = 1

        while True:
            while check > len(holder):
                holder.append(a)
                a += 1
            triangle.append(holder)
            holder = []
            check += 1
            
            if up_to in triangle[-1]: return triangle
            

print(floyd(up_to = 5)) 
print(floyd(n_row = 5))
print(floyd(up_to = 10)) 
print(floyd(n_row = 1)) 


'''
floyd(up_to = 5) ➞ [[1], [2, 3], [4, 5, 6]]
# The third row contains a 5.

floyd(n_row = 5) ➞[[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]
# Returns the first five rows.

floyd(up_to = 10) ➞ [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]

floyd(n_row = 1) ➞[[1]]
'''