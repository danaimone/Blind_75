class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = {c: [] for word in words for c in word}
        for first_word, second_word in zip(words, words[1:]):
            for first_char, second_char in zip(first_word, second_word):
                if first_char != second_char: 
                    adj_list[second_char].append(first_char)
                    break
            else:
                if len(second_word) < len(first_word):
                    return ""
        seen = {}
        alien_chars = []
        def dfs_visit(node):
            if node in seen: # we've entered a cycle
                return seen[node]
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
            
            
            