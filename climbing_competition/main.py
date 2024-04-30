from math import ceil


def climb(stamina:int, distances:list) -> int:
    moves:int = 0
    
    for i in range(1, len(distances)):
        if distances[i] - distances[i-1] > 0:
            if stamina < ceil(distances[i] - distances[i-1]) * 2: return moves
            stamina -= ceil(distances[i] - distances[i-1]) * 2
            moves += 1
        else:
            if stamina < ceil((distances[i] - distances[i-1]) * -1): return moves
            stamina -= ceil((distances[i] - distances[i-1]) * -1)
            moves += 1

    return moves


print(climb(5, [5, 4.2, 3, 3.5, 6, 4, 6, 8, 1]))
print(climb(10, [5, 4.2, 3, 3.5, 6, 4, 6, 8, 1]))


'''
climb(5, [5, 4.2, 3, 3.5, 6, 4, 6, 8, 1]) ➞ 3

climb(10, [5, 4.2, 3, 3.5, 6, 4, 6, 8, 1]) ➞ 3
'''