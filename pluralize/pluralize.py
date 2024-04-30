def pluralize(words:list) -> set:
    ans:list = []

    for i in words:
        if words.count(i) > 1: ans.append(i + 's')
        else: ans.append(i)

    return set(ans)


print(pluralize(["cow", "pig", "cow", "cow"]))
print(pluralize(["table", "table", "table"]))
print(pluralize(["chair", "pencil", "arm"]))


'''
pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }
'''