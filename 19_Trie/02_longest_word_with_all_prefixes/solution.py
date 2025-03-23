# https://leetcode.com/problems/longest-word-with-all-prefixes/
class TrieNode:
    def __init__(self):
        # List of 26 elements for each lowercase letter (a-z)
        self.children = [None] * 26
        # boolean flag to mark end of word
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def _char_to_index(self, char):
        # convert character to index
        return ord(char) - ord('a')
        
    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            ch_index = self._char_to_index(ch)
            if not current.children[ch_index]:
                current.children[ch_index] = TrieNode()
            current = current.children[ch_index]

        current.is_end_of_word = True
        

    def search(self, word: str) -> bool:
        current = self.root

        for ch in word:
            ch_index = self._char_to_index(ch)
            if not current.children[ch_index]:
                return False
            current = current.children[ch_index]

        return current.is_end_of_word
        
    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for ch in prefix:
            ch_index = self._char_to_index(ch)
            if not current.children[ch_index]:
                return False
            current = current.children[ch_index]

        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        # Initialize variables to track the longest valid word
        longest_word = ""

        for word in words:
            trie.insert(word)

        # Check each word
        for word in words:
            valid = True
            
            # Check if all prefixes of the word exist in the trie as complete words
            for i in range(1, len(word)):
                if not trie.search(word[:i]):
                    valid = False
                    break
            
            # If all prefixes exist and this word is better than our current best
            if valid:
                if len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word):
                    longest_word = word
        
        return longest_word

        