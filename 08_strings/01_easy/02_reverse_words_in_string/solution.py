class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        i = 0
        result_str = ""

        while i < n:
            while (i < n and s[i] == " "):
                i += 1

            # word begins here
            j = i
            while (j < n and s[j] != " "):
                j += 1

            # s[i:j] has subword
            if j == i:
                # no subword
                break
            if result_str:
                result_str = s[i:j] + " " + result_str
            else:
                result_str = s[i:j]

            i = j

        return result_str
    
s = Solution().reverseWords(" the sky is blue ")
print(f"Reversed string: |{s}|")