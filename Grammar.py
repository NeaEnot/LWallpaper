import random
import Alphabet


def generate(abc, l):
    answer = ''

    for i in range(l):
        ch = abc[random.randint(0, len(abc))]
        answer += ch

    return answer


def check(s):
    stk = 0

    for i in range(len(s)):
        ch = s[i]
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
        self.result = s


class Grammar:
    def __init__(self, alphabet, nr, rlmin, rlmax):
        self.alphabet = alphabet
        self.__dict__ = {}

        keys = [k for k in alphabet.dict.keys()]
        self.abc = ''
        for ch in keys:
            self.abc += ch

        for i in range(nr):
            key = keys[random.randint(0, len(keys))]

            if key != '[' and key != ']':
                keys.remove(key)
                self.__dict__.update({key: Rule(self.abc, rlmin, rlmax)})
            else:
                i -= 1

    def generate_axiom(self, l):
        answer = ']'

        while not check(answer):
            answer = ''
            for i in range(l):
                ch = self.abc[random.randint(0, len(self.abc))]
                answer += ch

        return answer

    def apply(self, axiom, iters):
        answer = axiom

        for i in range(iters):
            result = ''

            for ch in answer:
                if ch in self.__dict__.keys():
                    rule = self.__dict__[ch]
                    result += rule.result
                else:
                    result += ch

            answer = result
