# Q3. Write a function to check if a given string containing the characters (), {}, and [] is valid. A string is considered valid if all brackets are properly nested and closed.

def is_valid_brackets(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return False
        else:
            return False
    return not stack

strings = ["()", "([])", "{[()]}", "(]", "([)]", "{[]}", "[{()}]"]
for string in strings:
    print(f"{string}: {is_valid_brackets(string)}")
