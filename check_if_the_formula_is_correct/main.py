def formula(txt:str) -> bool:
    if txt == "": return None

    txt:list = txt.split('=')
    num_holder:list = []
    result:int = None

    for i in txt[0]:
        if i.isdigit(): num_holder.append(int(i))

    for i in txt[0]:
        if not i.isdigit() and i != ' ':
            if i == '+': result = num_holder[0] + num_holder[1]
            elif i == '/': result = num_holder[0] / num_holder[1]
            elif i == '*': result = num_holder[0] * num_holder[1]
            elif i == '-': result = num_holder[0] - num_holder[1]

    return int(txt[-1]) == result


print(formula("6 * 4 = 24"))
print(formula("18 / 17 = 2"))
print(formula(""))


'''
formula("6 * 4 = 24") ➞ True

formula("18 / 17 = 2") ➞ False

formula("") ➞ None
'''