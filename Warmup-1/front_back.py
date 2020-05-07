"""
Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""


def front_back(word):
    return word[len(word) - 1] + word[1:len(word)-1] + word[0] if len(word) > 1 else word


print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))
