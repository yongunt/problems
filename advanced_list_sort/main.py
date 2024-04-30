def advanced_sort(lst:list) -> list:
    ans:list = []

    for i in range(len(set(lst))): ans.append([])

    for i in lst:
        counter:int = 0

        while True:
            if ans[counter] == [] or i in ans[counter]:
                ans[counter].append(i)
                break

            counter+=1

    return ans


print(advanced_sort([2, 1, 2, 1]))
print(advanced_sort([5, 4, 5, 5, 4, 3]))
print(advanced_sort(["b", "a", "b", "a", "c"]))


'''
advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]

advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]

advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]
'''