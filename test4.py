def validPalindrome(self, s: str) -> bool:
    start = 0
    end = len(s)-1
    while start <= end:
        if s[start] != s[end]:
            string1 = s[:start]+s[start+1:]
            string2 = s[:end]+s[end+1:]
            return string1 == string1[::-1] or string2 == string2[::-1]
        start += 1
        end -= 1
    return True
