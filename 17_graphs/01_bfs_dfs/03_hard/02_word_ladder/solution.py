# https://leetcode.com/problems/word-ladder/description/
from collections import deque
from typing import *

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # we use bfs to store (word, steps) in queue
        queue = deque()

        # push beginWord in queue, and step size initially is 1
        queue.append((beginWord, 1))

        # add all elements to set.
        # as we visit them, we will delete them
        wordSet = set()
        for word in wordList:
            wordSet.add(word)

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for position in range(len(word)):
                for ch in range(ord('a'), ord('z') + 1):
                    modified_str = self.replaceCharAtPosition(word, chr(ch), position)

                    if modified_str in wordSet:
                        wordSet.remove(modified_str)
                        queue.append((modified_str, steps+1))

        # if there is no transformation sequence possible
        return 0

    def replaceCharAtPosition(self, string, ch, position):
        string_list = list(string)
        string_list[position] = ch
        return ''.join(string_list)

print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))