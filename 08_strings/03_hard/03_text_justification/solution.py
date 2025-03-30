# https://leetcode.com/problems/text-justification/
from typing import *

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # res is a list of line strings
        res = []
        # line is a temp variable that records words in a line (no space)
        # length is a temp variable that rcords length of all words (without space) in curr line
        line, length = [], 0
        i = 0

        while i < len(words):
            # case 1: Line complete
            # we know line is complete if
            # length + one_space_for_each_word_in_line + next_word > max_width
            # note: one_space_for_each_word = len(line)
            if length + len(line) + len(words[i]) > maxWidth:
                extra_space = maxWidth - length
                # ideally spaces = extra_spaces // len(line)-1
                # but we do max(1, len(line)-1), to take care of 1 word
                spaces = extra_space // max(1, len(line) - 1)
                remainder = extra_space % max(1, len(line) - 1)

                for j in range(max(1, len(line)-1)):
                    line[j] += " " * spaces

                    if remainder:
                        line[j] += " "
                        remainder -= 1

                res.append("".join(line))
                line, length = [], 0 # reset line and length

            # case 2: we have room for more word
            line.append(words[i])
            length += len(words[i])
            i += 1

        # handling last line
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        last_line += " " * trail_space
        res.append(last_line)

        return res

                