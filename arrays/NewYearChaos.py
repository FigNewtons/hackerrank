# TODO - not quite right. Variation on sorting
def minimum_bribes(queue):
    bribes = 0
    for rank, person in enumerate(queue, start=1):
        if rank >= person:
            continue
        elif person - rank > 2:
            return 'Too chaotic'
        else:
            bribes += person - rank
    return bribes


if __name__ == '__main__':
    print(minimum_bribes([2, 1, 5, 3, 4]))

'''
    1 2 3 4 5 6 7 8
    1 2 3 5 4 6 7 8  (5 b 4)
    1 2 5 3 4 6 7 8  (5 b 3)
    1 2 5 3 4 7 6 8  (7 b 6)
    1 2 5 3 7 4 6 8  (7 b 4)
    1 2 5 3 7 4 8 6  (8 b 6)
    1 2 5 3 7 8 4 6  (8 b 4)
    1 2 5 3 7 8 6 4  (6 b 4)


    1 2 5  3 7 8  6  4    


    1 2 3  4 5 6  7  8
    --------------------
    0 0 2 -1 2 2 -1 -4
    
'''