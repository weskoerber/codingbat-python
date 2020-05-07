"""
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3,
the front is whatever is there. Return a new string which is 3 copies of the front.

front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
"""


def front3(word):
    if len(word) > 3:
        length = 3
    else:
        length = len(word)

    new_word = ""
    for i in range(3):
        new_word = new_word + word[0:length]

    return new_word


print(front3('Java'))
print(front3('Chocolate'))
print(front3('abc'))
