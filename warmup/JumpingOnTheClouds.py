from typing import List


def jump(c: List[int], index: int) -> int:
    return index + 2 if index + 2 < len(c) and c[index + 2] == 0 else index + 1


def jumping_on_clouds(c: List[int]) -> int:
    index = 0
    jumps = 0
    while index != len(c) - 1:
        index = jump(c, index)
        jumps += 1
    return jumps


if __name__ == '__main__':
    print(jumping_on_clouds([0, 0, 0, 0, 1, 0]))
