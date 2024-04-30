def all_dividers(n:int) -> list:
    ans = []
    for i in range(1, n+1):
        if n%i == 0: ans.append(i)
    return ans


def simplify(string:str) -> str:
    string = string.split("/")
    firsts_dividers = all_dividers(int(string[0]))
    seconds_dividers = all_dividers(int(string[1]))

    for i in firsts_dividers:
        if i in seconds_dividers: gcd = i

    first_number = int(string[0])/gcd
    second_number = int(string[1])/gcd

    if first_number % second_number == 0: return str(int(first_number))
    else: return str(int(first_number)) + '/' + str(int(second_number))


print(simplify("4/6"))
print(simplify("10/11"))
print(simplify("100/400"))
print(simplify("8/4"))


'''
simplify("4/6") ➞ "2/3"

simplify("10/11") ➞ "10/11"

simplify("100/400") ➞ "1/4"

simplify("8/4") ➞ "2"
'''