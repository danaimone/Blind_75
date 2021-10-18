class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        Time Complexity: O(c) for every character relation
        Space Complexity: O(1) every relation must be represented and no additional space is used.
        :param words: list of words in lexicographic order
        :return: lexicographically ascending alien characters
        '''
        adj_list = {c: [] for word in words for c in word}
        for first_word, second_word in zip(words, words[1:]):
            for first_char, second_char in zip(first_word, second_word):
                if first_char != second_char: 
                    adj_list[second_char].append(first_char)
                    break
            else:
                if len(second_word) < len(first_word):
                    return ""
        seen = set()
        alien_chars = []
        def dfs_visit(node):
            if node in seen: # we've entered a cycle
                return
            seen[node] = False
            for child in adj_list[node]:
                result = dfs_visit(child)
                if not result:
                    return False
            seen[node] = True
            alien_chars.append(node)
            return True
        
        if not all(dfs_visit(node) for node in adj_list):
            return ""
        
        return "".join(alien_chars)
            
            
            