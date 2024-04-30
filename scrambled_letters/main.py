def scrambled(words:list, mask:str) -> list:
    ans:list = []
    
    for word in words:
        flag:bool = False

        if len(word) == len(mask):
            for w, m in zip(word, mask):
                if w == m or m == '*': flag = True
                else:
                    flag = False
                    break
    
        if flag: ans.append(word)

    return ans


print(scrambled(["red", "dee", "cede", "reed", "creed", "decree"], "*re**"))
print(scrambled(["red", "dee", "cede", "reed", "creed", "decree"], "***"))


'''
scrambled([”red”, “dee”, “cede”, “reed”, “creed”, “decree”], “*re**”) ➞ [“creed”]

scrambled([”red”, “dee”, “cede”, “reed”, “creed”, “decree”], “***”) ➞ [“dee”, “red”]
'''