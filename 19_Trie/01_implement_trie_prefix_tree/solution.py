# https://leetcode.com/problems/implement-trie-prefix-tree/
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
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)