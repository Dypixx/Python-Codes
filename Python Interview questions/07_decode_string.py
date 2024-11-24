# Q7. Decode a string encoded with numbers and brackets, like "3[a2[c]]", into "accaccacc"

def decode_string(s):
    stack = []
    current_num = 0
    current_str = ""
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ']':
            prev_str, repeat_count = stack.pop()
            current_str = prev_str + current_str * repeat_count
        else:
            current_str += char
    
    return current_str

encoded_string = "3[a2[c]]"
decoded_string = decode_string(encoded_string)
print("Decoded string:", decoded_string)
