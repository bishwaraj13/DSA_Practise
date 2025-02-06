# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numeral_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        prev_val = 0

        for index, ch in enumerate(s):
            ch_val = roman_numeral_dict[ch]
            value_to_add = ch_val

            if (index + 1) < len(s):
                next_val = roman_numeral_dict[s[index+1]]

                if next_val > ch_val:
                    value_to_add = -ch_val

            result += value_to_add

            # update prev_val
            prev_val = ch_val

        return result
