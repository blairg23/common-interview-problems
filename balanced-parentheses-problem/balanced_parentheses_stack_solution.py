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

Solution translated into Python from https://medium.com/@gianpaul.r/balanced-parentheses-problem-6306083bc10d

"""

def balanced(string):
    open_paren = '('
    closed_paren = ')'

    if len(string) % 2 == 1 or len(string) == 0:
        return False
  
    stacked = []

    if string[0] == closed_paren:
        return False

    for i in range(len(string)):
        if string[i] == open_paren:
          stacked.append(string[i])
        else:
            stacked.pop()

    if len(stacked) != 0:
        return False
    return True


if __name__ == '__main__':
    balanced_paren_strings = ['((()))', '(())', '()', '()()()']

    unbalanced_paren_strings = ['())', '))((', '()((']

    for balanced_paren_string in balanced_paren_strings:
        print('balanced_paren_string:', balanced_paren_string)
        assert balanced(string=balanced_paren_string) is True

    for unbalanced_paren_string in unbalanced_paren_strings:
        print('unbalanced_paren_string:', unbalanced_paren_string)
        assert balanced(string=unbalanced_paren_string) is False