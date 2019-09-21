"""
The Balanced Parentheses Problem.

https://bradfieldcs.com/algos/stacks/balanced-parentheses/

Given a string of parentheses, how to tell if they're balanced?

---

((({}[]))) -> true
((())) -> true
(()) -> true
() -> true
()()() -> true

---

()) -> false
))(( -> false
()(( -> false

---

Solution taken from https://bradfieldcs.com/algos/stacks/balanced-parentheses/

"""

OPENING = '('


def balanced(string):
    stack = []
    for paren in string:
        if paren == OPENING:
            stack.append(paren)
        else:
            try:
                stack.pop()
            except IndexError:  # too many closing parens
                return False
    return len(stack) == 0  # false if too many opening parens


if __name__ == '__main__':
    balanced_paren_strings = ['((()))', '(())', '()', '()()()']

    unbalanced_paren_strings = ['())', '))((', '()((']

    for balanced_paren_string in balanced_paren_strings:
        print('balanced_paren_string:', balanced_paren_string)
        assert balanced(string=balanced_paren_string) is True

    for unbalanced_paren_string in unbalanced_paren_strings:
        print('unbalanced_paren_string:', unbalanced_paren_string)
        assert balanced(string=unbalanced_paren_string) is False