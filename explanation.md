# Problem 1: LRU Cache
## Problem Statement
The goal is to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit.
## Choice of Data Structure
`collection.OrderedDict` is used for `cache` to build the LRU feature. When an item is get by the given `key`, this `key` `value` is moved into the end of the `OrderedDict` (most recently used). If the cache capacity (by default `5`) is reached, the least used item on the top of `OrderedDict` is removed from `cache`
## Time and Space Complexity
**Time complexity**

Using hash function, the time complexity of `get` and `set` operation of `OrderedDict` is constant O(1).  

**Space complexity:**

O(n), depending on the cache capacity

# Problem 2: File Recursion
## Problem Statement
The goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"
## Choice of Data Structure
Since each directory can have a number of files and sub-directories. The recursion approach is used here to walk through all directories and dive into sub-directories. If the directory contains the file with name extension `.c`, the function returns the full path to that file.
## Time and Space Complexity
**Time complexity**

Depending on the width `w`, the number of files/directories, and depth `d`, the number of recursive sub-directories, the time complexity is d*O(w)

**Space complexity**

Since all local variables will be released on function return, the space complexity is depending on the number of file paths the function returns -> O(n)

# Problem 3: Huffman Coding
## Problem Statement
Implement the Huffman Coding approach which is a lossless data compression algorithm.
## Choice of Data Structure
To build a huffman tree, a prioritized queue is used to save the unique characters and their frequencies in the string. Each node is linked to `left_child` (Huffman code `0`) and `right_child` (Huffman code `1`). Since the goal of tree traversal is to find a path from the root node to leaf nodes, the more efficient way here is to use Depth First Search approach.
## Time and Space Complexity
**Time complexity**

The time complexity for a tree build-up is n O(log n)

**Space complexity**

The space complexity is depending on the number of unique characters O(n)

# Problem 4: Active Directory
## Problem Statement
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids. This task is to write a function that provides an efficient look up of whether the user is in a group.
## Choice of Data Structure
Since each group may have a hug number of users and sub-groups, it is more efficient to perform a breath first search through the group tree. It will walk through the groups in the same hierachy. When the user is found, it will break the search, before diving into more depth.
## Time and Space Complexity
**Time complexity**

In worst-case, it will go through all groups represented by tree nodes, while for each group, it will check whether the user is in the group.(`user in group.get_users()`) the time complexity will be O(n) * O(n)

**Space complexity**

During the searching, a queue is used to store the node candidates. In worst-case all groups is stored there. Thus, the space complexity is O(n) 
# Problem 5: Blockchain
## Problem Statement
A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

This task is to implement a blockchain using a linked list.
## Choice of Data Structure
Each block is linked to the previous block in the block chain implemented by `LinkedList`
## Time and Space Complexity
**Time complexity**

The time complexity of appending a new block at the end of the chain is O(1)

**Space complexity**

Depending on the number of blocks added to the chain and the length of string in each block data, the space complexity would be n O(n)
# Problem 6: Union and Intersection
## Problem Statement
The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

It will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively.
## Choice of Data Structure
LinkedList with unique elements is used here. It reduces the time when converting it to a python `list`/`set` that are used to calculate union and intersection
## Time and Space Complexity
**Time complexity**

- `append` and `to_list`: O(n) It depends on the length of `LinkedList`
- `union` and `intersection`: nO(n) It depends on the length of `llist_1` and `llist_2`

**Space complexity**

The space complexity is determined by the length of union/intersection list O(n)