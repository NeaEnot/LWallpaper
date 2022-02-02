import random
import Alphabet


def generate(alphabet, l):
    abc = alphabet + '[]'
    answer = ''

    for i in range(l):
        ch = abc[random.randint(0, len(abc))]
        answer += ch

    return answer


def check(s):
    stk = 0

    for i in range(len(str)):
        ch = str[i]
        if ch == '[':
            stk += 1
        if ch == ']':
            stk -= 1

        if stk < 0:
            return False

    if stk > 0:
        return False
    else:
        return True


class Rule:
    def __init__(self, abc, minl, maxl):
        s = ']'
        while not check(s):
            s = generate(abc, random.randint(minl, maxl))
        self.rule = s
