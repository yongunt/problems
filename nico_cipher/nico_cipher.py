from math import ceil

def nico_cipher(message, key):
    key = list(key)
    message = list(message)
    check = ceil(len(message)/len(key))
    holder = sorted(key)
    my_dict = {}
    ans = ""

    for i in range(len(key)):
        if holder.index(key[i]) + 1 in my_dict.keys():
            my_dict[holder.index(key[i]) + 2] = []
            key[i] = holder.index(key[i]) + 2
            continue

        my_dict[holder.index(key[i]) + 1] = []
        key[i] = holder.index(key[i]) + 1



    while message != []:
        for j in range(len(key)):
            try:
                my_dict[key[j]].append(message[0])
                del message[0]
            except IndexError:
                my_dict[key[j]].append(" ")

    for i in range(check):
        for j in sorted(my_dict): ans += my_dict[j][i]

    return ans


print(nico_cipher("mubashirhassan", "crazy"))
print(nico_cipher("edabitisamazing", "matt"))
print(nico_cipher("iloveher", "612345"))


'''
nico_cipher("mubashirhassan", "crazy") ➞ "bmusarhiahass n"

nico_cipher("edabitisamazing", "matt") ➞ "deabtiismaaznig "

nico_cipher("iloveher", "612345") ➞ "lovehir    e"
'''