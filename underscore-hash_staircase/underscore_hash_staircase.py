def staircase(n):
    ans = ""

    if n > 0:
        for i in range(1, n+1): ans += ((n-i) * "_") + (i*"#") + "\n"
    elif n < 0:
        n = abs(n)
        a = 0

        for i in range(n, 0, -1):
            ans += (a * "_") + (i*"#") + "\n"
            a += 1

    return ans


print(staircase(3))
print(staircase(7))
print(staircase(2))
print(staircase(-8))


'''
staircase(3) ➞ "__#\n_##\n###"
__#
_##
###

staircase(7) ➞ "______#\n_____##\n____###\n___####\n__#####\n_######\n#######"
______#
_____##
____###
___####
__#####
_######
#######

staircase(2) ➞ "_#\n##"
_#
##

staircase(-8) ➞ "########\n_#######\n__######\n___#####\n____####\n_____###\n______##\n_______#"
########
_#######
__######
___#####
____####
_____###
______##
_______#
'''