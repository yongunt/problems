def sock_merchant(socks:list) -> int:
    ans:int = 0
    holder:dict = {}

    for i in socks: holder[i] = socks.count(i)

    for i in holder:
        if holder[i] >= 2: ans += holder[i] // 2

    return ans


print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))
print(sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]))
print(sock_merchant([]))


'''
sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]) ➞ 3

sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]) ➞ 4

sock_merchant([]) ➞ 0
'''