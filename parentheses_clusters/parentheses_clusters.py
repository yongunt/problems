def split(seq:str):
    ans = []
    left = 0
    right = 0
    last_index = 0


    for i in range(len(seq)):
        if seq[i] == "(": left += 1
        if seq[i] == ")": right += 1

        if left == right:
            left = 0
            right = 0
            ans.append(seq[last_index:i+1])
            last_index = i + 1 

    return ans


print(split("()()()"))
print(split("((()))"))
print(split("((()))(())()()(()())"))
print(split("((())())(()(()()))"))


'''
split("()()()") ➞ ["()", "()", "()"]

split("((()))") ➞ ["((()))"]

split("((()))(())()()(()())") ➞ ["((()))", "(())", "()", "()", "(()())"]

split("((())())(()(()()))") ➞ ["((())())", "(()(()()))"]
'''