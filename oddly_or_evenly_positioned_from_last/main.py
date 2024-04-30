def char_at_pos(x, y):
    if y == "even":        
        if isinstance(x, list):
            ans:list = []
            for i in range(1, len(x), 2):
                ans.append(x[i])
        elif isinstance(x, str):
            ans:str = ""
            for i in range(1, len(x), 2):
                ans += x[i]
        return ans
        
    else:
        if isinstance(x, list):
            ans:list = []
            for i in range(0, len(x), 2):
                ans.append(x[::-1][i])
        elif isinstance(x, str):
            ans:str = ""
            for i in range(0, len(x), 2):
                ans += x[::-1][i]
        return ans[::-1]


print(char_at_pos([2, 4, 6, 8, 10], "even"))
print(char_at_pos("EDABIT", "odd"))
print(char_at_pos([")", "(", "*", "&", "^", "%", "$", "#", "@", "!"], "odd"))


'''
char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
# 4 & 8 occupy the 4th & 2nd positions from right.

char_at_pos("EDABIT", "odd") ➞ "DBT"
# "D", "B" and "T" occupy the 5th, 3rd and 1st positions from right.

char_at_pos([")", "(", "*", "&", "^", "%", "$", "#", "@", "!"], "odd") ➞ ["(", "&", "%", "#", "!"]
'''