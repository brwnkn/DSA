def lengthOfLongestSubstring(s):
    start = 0
    sub_string = ""
    stringlist  = []

    for character in list(s):
        sub_string = s[start: s.index(character)]
        if character not in sub_string:
            stringlist.append(sub_string)
            start = s.index(character)

        else: 
            sub_string += str(character)
        print(f"substring: {sub_string} string list: {stringlist} ")
    return stringlist

print(lengthOfLongestSubstring("abcabcbb"))
