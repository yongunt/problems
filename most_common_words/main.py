from string import ascii_lowercase as alp
alp += ' '


def most_common_words(text:str, n:int) -> dict:
    refined_text:str = ""
    check:int = 0
    holder_dict:dict = {}
    ans:dict = {}
    key_holder:list = []
    value_holder:list = []
    refined_text_words:list = []

    for i in text:
        if i.lower() in alp: refined_text += i.lower()

    refined_text_words = refined_text.split(' ')

    for i in refined_text_words: holder_dict[i] = refined_text_words.count(i)

    for i in holder_dict: value_holder.append(holder_dict[i])
    value_holder = list(set(value_holder))[::-1]

    for i in value_holder:
        for j in holder_dict:
            if holder_dict[j] == i: key_holder.append(j)

    if n > len(key_holder):
        for i in key_holder:
            ans[i] = holder_dict[i]
        return ans
    else:
        for i in key_holder:
            ans[i] = holder_dict[i]
            
            check += 1
            
            if n == check: return ans


words = "How much wood could a woodchuck chuck If a woodchuck could chuck wood? As much wood as a woodchuck could chuck, If a woodchuck could chuck wood"

print(most_common_words(text=words, n=3))
print(most_common_words(text=words, n=7))
print(most_common_words(text=words, n=999))


'''
words = "How much wood could a woodchuck chuck If a woodchuck could chuck wood? As much wood as a woodchuck could chuck, If a woodchuck could chuck wood"

most_common_words(text=words, n=3) ➞ {
  "wood": 4,
  "could": 4,
  "a": 4
}

most_common_words(text=words, n=7) ➞ {
  "wood": 4,
  "could": 4,
  "a": 4,
  "woodchuck": 4,
  "chuck": 4,
  "much": 2,
  "if": 2
}

most_common_words(text=words, n=999) ➞ {
  "wood": 4,
  "could": 4,
  "a": 4,
  "woodchuck": 4,
  "chuck": 4,
  "much": 2,
  "if": 2,
  "as": 2,
  "how": 1
}
'''