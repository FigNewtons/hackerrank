from typing import List
from collections import Counter


def check_magazine(magazine: List[str], note: List[str]) -> str:
    words = Counter(magazine)
    for word in note:
        if word not in words:
            return 'No'
        else:
            words[word] -= 1
            if words[word] == 0:
                del words[word]

    return 'Yes'


if __name__ == '__main__':
    magazine = 'two times three is not four'.split()
    note = 'two times two is four'.split()
    print(check_magazine(magazine, note))
