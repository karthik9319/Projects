import sys
from typing import Dict

if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

char_dict = {}  # type: Dict[str, int]


def char_count(string: str) -> dict:
    new_string = string.lower()
    for c in new_string:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict


if __name__ == "__main__":
    UserString = str(input("Enter Input String: "))
    CharCount = char_count(UserString)
    print("Characters Count: ", CharCount)
