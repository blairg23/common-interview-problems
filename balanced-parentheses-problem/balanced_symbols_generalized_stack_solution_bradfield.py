"""
The Generalized Balanced Symbols Problem.

https://bradfieldcs.com/algos/stacks/balanced-parentheses/

Given a string of opening and closing symbols, how to tell if they're balanced?

---

((({}[]))) -> true
((())) -> true
(()) -> true
() -> true
()()() -> true
()[]{} -> true
([{}]) -> true

---

()) -> false
))(( -> false
()(( -> false
([{]}) -> false

---

Solution taken from https://bradfieldcs.com/algos/stacks/balanced-parentheses/

"""

PAIRINGS = {
    '(': ')',
    '{': '}',
    '[': ']'
}

def balanced(string):
    stack = []
    for s in string:
        if s in PAIRINGS:
            stack.append(s)
            continue
        try:
            expected_opening_symbol = stack.pop()
        except IndexError:  # too many closing symbols
            return False
        if s != PAIRINGS[expected_opening_symbol]:  # mismatch
            return False
    return len(stack) == 0  # false if too many opening symbols


if __name__ == '__main__':
    balanced_paren_strings = ['((()))', '(())', '()', '()()()', r'()[]{}', r'([{}])']

    unbalanced_paren_strings = ['())', '))((', '()((', r'([{]})']

    for balanced_paren_string in balanced_paren_strings:
        print('balanced_paren_string:', balanced_paren_string)
        assert balanced(string=balanced_paren_string) is True

    for unbalanced_paren_string in unbalanced_paren_strings:
        print('unbalanced_paren_string:', unbalanced_paren_string)
        assert balanced(string=unbalanced_paren_string) is False