import sys

class Node:
    def __init__(self, character=None, frequency=None):
        self.character = character
        self.frequency = frequency
        self.left_child = None
        self.right_child = None
        self.code = None
    
    def has_left_child(self):
        return self.left_child is not None

    def has_right_child(self):
        return self.right_child is not None

    def set_left_child(self, node):
        node.code = '0'
        self.left_child = node
    
    def set_right_child(self, node):
        node.code = '1'
        self.right_child = node

    def is_equal_to(self, character):
        return self.character == character

    def has_character(self):
        return self.character is not None

    def __repr__(self):
        return 'character: {} frequency: {}'.format(self.character, self.frequency)

class PriorityQueue:
    def __init__(self):
        self.queue = list()

    def enque(self, node):
        for idx, item in enumerate(self.queue):
            if node.frequency < item.frequency:
                self.queue.insert(idx, node)
                return

        self.queue.append(node)

    def deque(self):
        return self.queue.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return self.__len__() == 0

    def __len__(self):
        return len(self.queue)

    def __repr__(self):
        output_str = '========== Priority Queue =========\n'
        for item in self.queue:
            output_str += '{}\n'.format(item)
        output_str += '==================================='
        return output_str

class HuffmanTree:
    def __init__(self):
        self.root = None

    def build(self, queue):
        if queue.is_empty():
            print('Warning. The given PriorityQueue is empty.')
            return

        while len(queue) > 1:
            node = self.__calculate_parent(queue.deque(), queue.deque())
            queue.enque(node)
        self.root = queue.deque()

    def __calculate_parent(self, left_child, right_child):
        if left_child is None:
            return None
        
        if right_child is None:
            return left_child
        
        parent = Node(frequency = left_child.frequency + right_child.frequency)
        parent.set_left_child(left_child)
        parent.set_right_child(right_child)

        return parent

def get_priority_queue(string):
    character_frequency = dict()
    for char in string:
        character_frequency[char] = character_frequency.get(char, 0) + 1
    
    queue = PriorityQueue()
    for char in character_frequency:
        node = Node(character=char, frequency=character_frequency[char])
        queue.enque(node)

    return queue

def traversal_tree(parent_node, stack, char):
    if parent_node:
        stack.append(parent_node)
        if parent_node.is_equal_to(char):
            return True
        else:
            if traversal_tree(parent_node.left_child, stack, char):
                return True
            if traversal_tree(parent_node.right_child, stack, char):
                return True
            stack.pop()

def find_char_in_tree(tree, char):
    stack = list()
    traversal_tree(tree.root, stack, char)
    huffman_code = ''
    for item in stack:
        if item.code is not None:
            huffman_code += item.code
    return huffman_code, stack

def huffman_encoding(data):
    queue = get_priority_queue(data)
    tree = HuffmanTree()
    tree.build(queue)

    huffman_code = ''
    for char in data:
        char_code, _ = find_char_in_tree(tree, char)
        huffman_code += char_code

    return huffman_code, tree

def huffman_decoding(data, tree):
    node = tree.root
    output_string = ''
    for bit in data:
        if bit == '0':
            node = node.left_child
        elif bit == '1':
            node = node.right_child

        if node is not None and node.has_character():
            output_string += node.character
            node = tree.root

    return output_string

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

###################################################################################################
########################################   TEST   #################################################
###################################################################################################

def test_queue():
    print('\n--------------------   TEST_QUEUE   ------------------')

    queue = PriorityQueue()
    print(queue.deque())                             # return None, since no item exists in queue

    queue.enque(Node(character='A', frequency=5))
    queue.enque(Node(frequency=2))
    queue.enque(Node(frequency=9))
    queue.enque(Node(character='B', frequency=5))
    print(queue)                                     # print items with frequency [2, 5, 5, 9]
                                                     # nodes in queue is ordered by frequency. 
                                                     # low frequency has high priority
    queue.deque()
    print(queue)                                     # print items with frequency [5, 5, 9]
                                                     # the item with highest priority (lowest frequency) is removed by deque()

    print('--------------------   END: TEST_QUEUE   ------------------\n')


def test_get_priority_queue():
    print('\n--------------------   TEST_GET_PRIORITY_QUEUE   ------------------')

    a_great_sentence = 'The bird is the word'
    print(get_priority_queue(a_great_sentence))      # print priority queue with character frequencies
    print(get_priority_queue(''))                    # empty queue caused by empty string

    print('--------------------   END: TEST_GET_PRIORITY_QUEUE   ------------------\n')

def test_tree():
    print('\n--------------------   TEST_TREE  ------------------')

    a_great_sentence = 'AAAAAAABBBCCCCCCCDDEEEEEE'
    queue = get_priority_queue(a_great_sentence)
    print(queue)
    tree = HuffmanTree()
    tree.build(queue)

    for char in set(a_great_sentence):
        print('Traversal tree for {}:'.format(char))                         # Show the traversal through the tree -> Depth First Search
        huffman_code, found_path = find_char_in_tree(tree, char)
        print('\nPath Found for {}:'.format(char))
        print(*found_path, sep=' -> ')

        print('\nHuffman Code for character {}: {}\n'.format(char, huffman_code))
    
    print('--------------------   END: TEST_TREE   ------------------\n')

def test_huffman_encoding():
    print('\n--------------------   TEST_HUFFMAN_ENCODING  ------------------')
    huffman_code, _ = huffman_encoding('AAAAAAABBBCCCCCCCDDEEEEEE')
    if huffman_code == '1010101010101000100100111111111111111000000010101010101':
        print('Pass')
    else:
        print('Failed')
    print('--------------------   END: TEST_HUFFMAN_ENCODING   ------------------\n')

def test_huffman_decoding():
    print('\n--------------------   TEST_HUFFMAN_DECODING  ------------------')
    data = 'AAAAAAABBBCCCCCCCDDEEEEEE'
    huffman_code, tree = huffman_encoding(data)
    decoded_string = huffman_decoding(huffman_code, tree)
    if decoded_string == data:
        print('Pass')
    else:
        print('Failed. Output: {}, Expected: {}'.format(decoded_string, data))
    print('--------------------   END: TEST_HUFFMAN_DECODING   ------------------\n')

def TEST_SUITE():
    test_queue()
    test_get_priority_queue()
    test_tree()
    test_huffman_encoding()
    test_huffman_decoding()

####################################################################################################