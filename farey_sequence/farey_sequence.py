def farey(n:int) -> list:
    result_holder:dict = {0:"0/1", 1:"1/1"}
    ans:list = []

    for i in range(n):
        for j in range(1, n+1):
            if i/j not in result_holder.keys() and i/j < 1:
                result_holder[i/j] = str(i) + '/' + str(j)

    for i in sorted(result_holder): ans.append(result_holder[i])

    return ans


print(farey(1))
print(farey(4))
print(farey(5))


'''
farey(1) ➞ ["0/1", "1/1"]

farey(4) ➞ ["0/1", "1/4", "1/3", "1/2", "2/3", "3/4", "1/1"]

farey(5) ➞ ["0/1", "1/5", "1/4", "1/3", "2/5", "1/2", "3/5", "2/3", "3/4", "4/5", "1/1"]
'''