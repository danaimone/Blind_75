
## Array

- [x] [Two Sum](https://leetcode.com/problems/two-sum/)
  - **Optimal O(n)**: `check whether complement (target - nums[i]) exists in a hashtable. if it does, return i and the complement key`
- [x] [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
  - **O(n)**: `keep track of max profit and min cost, max starts as inf, for each price our profit is the current price
  minus the min cost, check max_profit = max(profit, max_profit). min_cost = min(prices[i], min_cost)`
- [x] [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
  - **Cheese Way**: `create set from nums, return whether the set is different from how many nodes were given.`
  - **O(n)**: `use a hash table, if num is in hashtable, return False. otherwise true`
- [x] [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
  - **Naive (O(n^2)):** `Brute force from any given n by traversing left and right for each element.`
  - **O(n):** ` Build two arrays for all products up to i from left and all products up to i from right. At each element
    i, we know all the product [i-1...0] and all the products [i + 1...len(A)], so replace index with a 
    multiplication of these two elements.`
- [ ] [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- [ ] [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
- [ ] [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- [ ] [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- [ ] [3Sum](https://leetcode.com/problems/3sum/)
- [ ] [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

---

## Binary

- [ ] [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)
- [ ] [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
- [ ] [Counting Bits](https://leetcode.com/problems/counting-bits/)
- [ ] [Missing Number](https://leetcode.com/problems/missing-number/)
- [ ] [Reverse Bits](https://leetcode.com/problems/reverse-bits/)

---

## Dynamic Programming

- [x] [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [ ] [Coin Change](https://leetcode.com/problems/coin-change/)
- [ ] [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
- [ ] [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
- [ ] [Word Break Problem](https://leetcode.com/problems/word-break/)
- [ ] [Combination Sum](https://leetcode.com/problems/combination-sum-iv/)
- [ ] [House Robber](https://leetcode.com/problems/house-robber/)
- [ ] [House Robber II](https://leetcode.com/problems/house-robber-ii/)
- [ ] [Decode Ways](https://leetcode.com/problems/decode-ways/)
- [ ] [Unique Paths](https://leetcode.com/problems/unique-paths/)
- [ ] [Jump Game](https://leetcode.com/problems/jump-game/)

---

## Graph - :heavy_check_mark: on :date: 10/17/2021, review 10/25

- [x] [Clone Graph](https://leetcode.com/problems/clone-graph/)
- [x] [Course Schedule](https://leetcode.com/problems/course-schedule/)
- [x] [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
- [x] [Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [x] [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
- [x] [Alien Dictionary (Leetcode Premium)](https://leetcode.com/problems/alien-dictionary/)
- [x] [Graph Valid Tree (Leetcode Premium)](https://leetcode.com/problems/graph-valid-tree/)
- [x] [Number of Connected Components in an Undirected Graph (Leetcode Premium)](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

---

## Interval

- [ ] [Insert Interval](https://leetcode.com/problems/insert-interval/)
- [ ] [Merge Intervals](https://leetcode.com/problems/merge-intervals/)
- [ ] [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
- [ ] [Meeting Rooms (Leetcode Premium)](https://leetcode.com/problems/meeting-rooms/)
- [ ] [Meeting Rooms II (Leetcode Premium)](https://leetcode.com/problems/meeting-rooms-ii/)

---

## Linked List

- [x] [Reverse a Linked List](https://leetcode.com/problems/reverse-linked-list/)
  - **O(n):** `current pointer to head, previous pointer is nil. while current not none, the next node becomes previous,
    the previous pointer becomes the current node, and current node becomes the next node (requires temp pointer from current.next at top)
    prev would point to the head of this list`
- [x] [Detect Cycle in a Linked List](https://leetcode.com/problems/linked-list-cycle/)
  - **O(n):** `we can think of a fast and slow pointer approach where if there's a cycle, the fast pointer has to catch up to slow eventually. just keep moving them
          forward while slow != fast. if we ever hit a None with fast, there couldn't have been a cycle since there isn't anywhere to loop.`
- [x] [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- [x] [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
  - **O(n):** `put all the linked lists in a heap and pop the min off while you still have nodes. we can track both the value
  and the index of the node so we can maintain stability. keep popping and creating a new node, setting up the next pointers
    correctly. we can use that index that we tracked to update the original list so we can keep iterating through. if
    we successfully get another node, we can push that to our heap.`
- [x] [Remove Nth Node From End Of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
  - **O(n):** `we can send a fast pointer to go n times using the relation size of list - n + 1 as the actual index. We can send a fast pointer to the end of the index and 
    increment our slow pointer until it points to the element before n. we can do this by setting fast to our next pointer while now incrementing our slow pointer, and setting our slow's next to be its slow.next.next. Could potentially want to free the Nth node for memory purposes`
- [ ] [Reorder List](https://leetcode.com/problems/reorder-list/)

---

## Matrix

- [x] [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
  - **O(n):** `to do this in place, we can use two sets to check whether a zero was set for row or col. can alternatively
               set first element of row and first element of column as flags, and check if they are set. `
- [ ] [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
- [ ] [Rotate Image](https://leetcode.com/problems/rotate-image/)
- [ ] [Word Search](https://leetcode.com/problems/word-search/)

---

## String

- [ ] [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [ ] [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
- [ ] [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- [ ] [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- [ ] [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- [ ] [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [ ] [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- [ ] [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [ ] [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
- [ ] [Encode and Decode Strings (Leetcode Premium)](https://leetcode.com/problems/encode-and-decode-strings/)

---

## Tree
- [ ] [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [ ] [Same Tree](https://leetcode.com/problems/same-tree/)
- [ ] [Invert/Flip Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
- [ ] [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- [ ] [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [ ] [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
- [ ] [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)
- [ ] [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- [ ] [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- [ ] [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- [ ] [Lowest Common Ancestor of BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- [ ] [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
- [ ] [Add and Search Word](https://leetcode.com/problems/add-and-search-word-data-structure-design/)
- [ ] [Word Search II](https://leetcode.com/problems/word-search-ii/)

---

## Heap

- [x] [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [x] [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- [ ] [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

## Important Link:
[14 Patterns to Ace Any Coding Interview Question](https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed)
