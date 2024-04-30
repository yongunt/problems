def get_space_indexes(txt:str) -> list[int]:
    holder:list[int] = []
    for i in range(len(txt)):
        if txt[i] == ' ': holder.append(i)
    return holder


def get_uppercase_indexes(txt:str) -> list[int]:
    holder:list[int] = []
    for i in range(len(txt)):
        if txt[i].upper() == txt[i] and txt[i] != ' ': holder.append(i)
    return holder


def special_reverse_string(txt:str) -> str:
    lowercase_reversed_txt_items:str = [i.lower() for i in txt if i != ' '][::-1]
    index_of_spaces:list[int] = get_space_indexes(txt)
    index_of_uppercases:list[int] = get_uppercase_indexes(txt)
    ans:str = ""
    counter:int = 0
    
    while lowercase_reversed_txt_items != []:
        if counter in index_of_spaces:
            ans += ' '
        elif counter in index_of_uppercases:
            ans += lowercase_reversed_txt_items[0].upper()
            lowercase_reversed_txt_items.pop(0)
        else:
            ans += lowercase_reversed_txt_items[0]
            lowercase_reversed_txt_items.pop(0)
        
        counter += 1
    
    return ans


print(special_reverse_string("Edabit"))
print(special_reverse_string("UPPER lower"))
print(special_reverse_string("1 23 456"))


'''
special_reverse_string("Edabit") ➞ "Tibade"

special_reverse_string("UPPER lower") ➞ "REWOL reppu"

special_reverse_string("1 23 456") ➞ "6 54 321"
'''