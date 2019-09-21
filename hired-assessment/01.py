"""
Given a lowercase string, s, return the index fo the first character that appears just once in a string. 

If every character appears more than once, return -1

Example input:

s: "Who wants hot watermelon?"

Example Output:

8

Explanation:

"who wants hot watermelon?"
         ^
 012345678

 The first charactter that appears only once is "s" and it appears at index 8.
"""

def solution(s):
    # Type your solution here
    has_been_seen = {}
    for i in range(len(s)):
        if s[i] not in has_been_seen:
            has_been_seen[s[i]] = 0
        has_been_seen[s[i]] += 1

    for i in range(len(s)):
        if has_been_seen[s[i]] == 1:
            return i
    return -1
        

if __name__ == '__main__':
    s = "who wants hot watermelon?"
    print(solution(s=s))