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
()[]{} -> true
([{}]) -> true

---

()) -> false
))(( -> false
()(( -> false
([{]}) -> false

---

In the naive solution,

This works:
((({}[]))) -> true
()) - > false

But how to solve this?
([{]}) -> false

"""



def balanced(string):
    open_char = '('
    close_char = ')'
    opens_and_closes = []
    for i in range(len(string)):
        if i == 0 and string[i] == close_char:
            return False
        else:
            if string[i] == open_char:
                opens_and_closes.append('open')
            elif string[i] == close_char:
                opens_and_closes.append('close')
            else:
                raise Exception()
        
    if opens_and_closes.count('open') == opens_and_closes.count('close'):
        return True
    return False
                
            
if __name__ == '__main__':
    balanced_paren_strings = ['((()))', '(())', '()', '()()()']

    unbalanced_paren_strings = ['())', '))((', '()((']

    for balanced_paren_string in balanced_paren_strings:
        print('balanced_paren_string:', balanced_paren_string)
        assert balanced(string=balanced_paren_string) is True

    for unbalanced_paren_string in unbalanced_paren_strings:
        print('unbalanced_paren_string:', unbalanced_paren_string)
        assert balanced(string=unbalanced_paren_string) is False