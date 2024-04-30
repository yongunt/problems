def shift_letters(word:str, times:int):
    space_holder = []
    holder = ""
    check = 0

    word = list(word)

    for i in word:
        if i == " ":
            space_holder.append(word.index(i))
            del word[word.index(i)]
    
    for i in range(times):
        holder = word[-1]
        del word[-1]
        word.insert(0, holder)

    for i in space_holder:
        word.insert(i+check, " ")
        check += 1

    return "".join(word)


print(shift_letters("Boom", 2))
print(shift_letters("This is a test",  4))
print(shift_letters("A B C D E F G H", 5))


'''
shift_letters("Boom", 2) ➞ "omBo"

shift_letters("This is a test",  4) ➞ "test Th i sisa"

shift_letters("A B C D E F G H", 5) ➞  "D E F G H A B C"
'''