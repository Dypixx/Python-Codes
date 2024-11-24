# Q11. Determine if a string can be segmented into a sequence of dictionary words.

def word_break(s, word_dict):
    word_set = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]

s = "applepenapple"
word_dict = ["apple", "pen"]
print(word_break(s, word_dict))  # Output: True

s = "catsandog"
word_dict = ["cats", "dog", "sand", "and", "cat"]
print(word_break(s, word_dict))  # Output: False
