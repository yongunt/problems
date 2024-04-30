def find_max(ls:list) -> tuple:
    max:str = ""
    max_count:int = 0
    votes_holder:dict = {}

    for i in ls: votes_holder[i] = ls.count(i)

    for i in ls:
        if votes_holder[i] > max_count:
            max = i
            max_count = votes_holder[i]

    return (max,max_count)


def majority_vote(votes:list) -> None:
    ans:str = find_max(votes)[0]
    ans_count = find_max(votes)[1]

    for i in votes:
        if i != ans and ans_count == votes.count(i): return None

    return ans


print(majority_vote(["A", "A", "B"]))
print(majority_vote(["A", "A", "A", "B", "C", "A"]))
print(majority_vote(["A", "B", "B", "A", "C", "C"]))


'''
majority_vote(["A", "A", "B"]) ➞ "A"

majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"

majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None
'''