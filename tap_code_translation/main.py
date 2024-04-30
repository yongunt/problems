letters:list[str] = "a b ck d e f g h i j l m n o p q r s t u v w x y z".split(" ")
table:list[list[str]] = []

for i in range(5):
    temp:list[str] = []
    for j in range(5):        
        temp.append(letters[0])
        letters.pop(0)
    table.append(temp)


def get_letter_by_index(msg:list[str]) -> str:
    if (len(msg[0]) - 1) == 0 and (len(msg[1]) - 1) == 2: return 'c'
    return table[len(msg[0]) - 1][len(msg[1]) - 1]


def get_letters_index(letter:str) -> tuple:
    for i in range(len(table)):
        for j in range(len(table)):
            if letter == table[i][j] or letter in table[i][j]: return (i+1, j+1)


def tap_code(txt:str) -> str:
    ans:str = ""

    if txt[0] == '.':
        txt:list[str] = txt.split(' ')
        txt:list[list[str]] = [(txt[i-1] + ' ' + txt[i]).split(' ') for i in range(1, len(txt), 2)]
        for msg in txt: ans += get_letter_by_index(msg)
        return ans
    else:
        for letter in txt:
            temp:tuple = get_letters_index(letter)
            ans += ('.' * temp[0]) + ' ' + ('.' * temp[1]) + ' '
        return ans[:len(ans)-1]


print(tap_code("break"))
print(tap_code(".... ... ... ..... . ..... ... ... .... ...."))


'''
tap_code("break") ➞ ". .. .... .. . ..... . . . ..."

tap_code(".... ... ... ..... . ..... ... ... .... ....") ➞ "spent"
'''