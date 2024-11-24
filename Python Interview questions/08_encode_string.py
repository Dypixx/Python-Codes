# Q8. You are given a string "s" consisting of lowercase letters. Your task is to encode the string in a compressed form where repeated characters are grouped together, and the count of those characters is included in square brackets.

def encode_string(s):
    encoded_str = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            if count > 1:
                encoded_str += str(count) + "[" + s[i - 1] + "]"
            else:
                encoded_str += s[i - 1]
            count = 1
    if count > 1:
        encoded_str += str(count) + "[" + s[-1] + "]"
    else:
        encoded_str += s[-1]

    return encoded_str

string = "aaabbccccdaa"
encoded_string = encode_string(string)
print("Encoded string:", encoded_string)
