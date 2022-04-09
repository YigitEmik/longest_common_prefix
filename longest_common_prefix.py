
# Longest Common Prefix Problem
# https://leetcode.com/problems/longest-common-prefix/

strs = ['flower', 'flow', 'flight']
def longestCommonPrefix(alist) -> str:
    output = ""

    for i in range(len(alist[0])):
        for s in alist:
            if i == len(s) or s[i] != alist[0][i]:
                return output
        output += strs[0][i]
    return output

print(longestCommonPrefix(strs))