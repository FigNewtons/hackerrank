from typing import Dict, Set


def index_dict(s: str) -> Dict[str, Set[int]]:
    d = {}
    for index, ch in enumerate(s):
        if ch in d:
            d[ch].add(index)
        else:
            d[ch] = set()
    return d


def common_substring(s1: str, s2: str) -> str:
    letters = set(s1)
    for ch in s2:
        if ch in letters:
            return 'YES'
    return 'NO'


if __name__ == '__main__':
    print(common_substring("hello", "world"))
