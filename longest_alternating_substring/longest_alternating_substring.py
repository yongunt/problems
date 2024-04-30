def check_order(num:str) -> bool:
    flag:bool = False

    for k in range(1, len(num)):
        if int(num[k-1]) % 2 == 0 and int(num[k]) % 2 == 0:
            flag = False
            break
        elif int(num[k-1]) % 2 != 0 and int(num[k]) % 2 != 0:
            flag = False
            break
        else:
            flag = True

    return flag


def longest_substring(number:str) -> str:
    holder:list = []
    ans:str = ""
    current_len:int = 0

    for i in range(len(number)):
        for j in range(1, len(number[i::]) + 1):
            if check_order(number[i::][0:j]): holder.append(number[i::][0:j])
    
    for i in holder:
        if len(i) > current_len:
            current_len = len(i)
            ans = i

    return ans


print(longest_substring("225424272163254474441338664823"))
print(longest_substring("594127169973391692147228678476"))
print(longest_substring("721449827599186159274227324466"))


'''
longest_substring("225424272163254474441338664823") ➞ "272163254"
# substrings = 254, 272163254, 474, 41, 38, 23

longest_substring("594127169973391692147228678476") ➞ "16921472"
# substrings = 94127, 169, 16921472, 678, 476

longest_substring("721449827599186159274227324466") ➞ "7214"
# substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
# 7214 and 9274 have same length, but 7214 occurs first.
'''