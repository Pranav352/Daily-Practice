


def longest_substring(s):
    max_length = 0

    for i in range(len(s)):
        find = ""

        for j in range(i,len(s)):
            if s[j] not in find:
                find = find + s[j]
            else:
                break
            if len(find) > max_length:
                max_length = len(find)
    return max_length
print(longest_substring("abcabcbb"))




