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

    def is_leaf(self):
        return not self.has_left_child() and not self.has_right_child()

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

    if len(stack) == 1:
        return '0', stack

    for item in stack:
        if item.code is not None:
            huffman_code += item.code
    return huffman_code, stack

def huffman_encoding(data):
    if data is None or len(data) == 0 or type(data) is not str:
        print('!!! Invalid input data. It should be non-empty string!!!')
        return '', None
    queue = get_priority_queue(data)
    tree = HuffmanTree()
    tree.build(queue)

    huffman_code = ''
    for char in data:
        char_code, _ = find_char_in_tree(tree, char)
        huffman_code += char_code

    return huffman_code, tree

def huffman_decoding(data, tree):
    if (data is None) or (tree is None) or (len(data) == 0) or (type(data) is not str):
        print('!!! Invalid input data. It should be non-empty string!!!')
        return ''
    else:
        for char in data:
            if char not in ['0', '1']:
                print('!!! Invalid character {} in input data.!!!'.format(char))
                return ''

    node = tree.root
    output_string = ''
    for bit in data:
        if bit == '0':
            if node.has_left_child():
                node = node.left_child
        elif bit == '1':
            node = node.right_child

        if node is not None and node.has_character():
            output_string += node.character
            node = tree.root

    return output_string


########################################   TEST   #################################################
def test_empty_queue():
    print('\n--------------------   TEST_EMPTY_QUEUE   ------------------')

    queue = PriorityQueue()
    print(queue.deque())                             # return None, since no item exists in queue

    print('--------------------   END: TEST_EMPTY_QUEUE   ------------------\n')

def test_queue():
    print('\n--------------------   TEST_QUEUE   ------------------')

    queue = PriorityQueue()
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

def test_get_priority_queue_empty():
    print('\n--------------------   TEST_GET_PRIORITY_QUEUE_EMPTY   ------------------')

    print(get_priority_queue(''))                    # empty queue caused by empty string
    
    print('--------------------   END: TEST_GET_PRIORITY_QUEUE_EMPTY   ------------------\n')

def test_get_priority_queue():
    print('\n--------------------   TEST_GET_PRIORITY_QUEUE   ------------------')

    a_great_sentence = 'The bird is the word'
    
    # print priority queue with character frequencies
    # character: T frequency: 1
    # character: b frequency: 1
    # character: s frequency: 1
    # character: t frequency: 1
    # character: w frequency: 1
    # character: o frequency: 1
    # character: h frequency: 2
    # character: e frequency: 2
    # character: i frequency: 2
    # character: r frequency: 2
    # character: d frequency: 2
    # character:   frequency: 4
    print(get_priority_queue(a_great_sentence))

    print('--------------------   END: TEST_GET_PRIORITY_QUEUE   ------------------\n')

def test_tree():
    print('\n--------------------   TEST_TREE  ------------------')

    a_great_sentence = 'AAAAAAABBBCCCCCCCDDEEEEEE'
    queue = get_priority_queue(a_great_sentence)
    print(queue)
    tree = HuffmanTree()
    tree.build(queue)

    # The characters with expected huffman code:
    # C -> 11
    # D -> 000
    # B -> 001
    # E -> 01
    # A -> 10
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

    # The result of encoding must be same as the given code from example
    if huffman_code == '1010101010101000100100111111111111111000000010101010101':
        print('Pass')
    else:
        print('Failed')
    print('--------------------   END: TEST_HUFFMAN_ENCODING   ------------------\n')

def test_huffman_decoding():
    print('\n--------------------   TEST_HUFFMAN_DECODING  ------------------')
    
    data = 'The bird is the word'

    print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print ("The content of the data is: {}\n".format(data))
    
    huffman_code, tree = huffman_encoding(data)
    
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(huffman_code, base=2))))
    print ("The content of the encoded data is: {}\n".format(huffman_code))

    decoded_string = huffman_decoding(huffman_code, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_string)))
    print ("The content of the encoded data is: {}\n".format(decoded_string))

    # The decoded string must be same as the given input data
    if decoded_string == data:
        print('Pass')
    else:
        print('Failed. Output: {}, Expected: {}'.format(decoded_string, data))
    
    print('--------------------   END: TEST_HUFFMAN_DECODING   ------------------\n')

def test_huffman_decoding_repetitive_data():
    print('\n--------------------   TEST_HUFFMAN_DECODING_REPETITIVE_DATA  ------------------')
    
    data = 'AAAAAAA'

    print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print ("The content of the data is: {}\n".format(data))

    huffman_code, tree = huffman_encoding(data)
    
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(huffman_code, base=2))))
    print ("The content of the encoded data is: {}\n".format(huffman_code))
    
    decoded_string = huffman_decoding(huffman_code, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_string)))
    print ("The content of the encoded data is: {}\n".format(decoded_string))

    # The decoded string must be same as the given input data
    if decoded_string == data:
        print('Pass')
    else:
        print('Failed. Output: {}, Expected: {}'.format(decoded_string, data))
    
    print('--------------------   END: TEST_HUFFMAN_DECODING_REPETITIVE_DATA   ------------------\n')

def test_huffman_decoding_empty_data():
    print('\n--------------------   TEST_HUFFMAN_DECODING_EMPTY_DATA  ------------------')
    
    data = ''

    huffman_code, tree = huffman_encoding(data)            # output error message: !!! Invalid input data. It should be non-empty string!!!
    decoded_string = huffman_decoding(huffman_code, tree)  # output error message: !!! Invalid input data. It should be non-empty string!!!

    # The decoded string must be same as the given input data
    if decoded_string == data:
        print('Pass')
    else:
        print('Failed. Output: {}, Expected: {}'.format(decoded_string, data))
    
    print('--------------------   END: TEST_HUFFMAN_DECODING_EMPTY_DATA   ------------------\n')

def TEST_SUITE():
    test_queue()
    test_empty_queue()
    test_get_priority_queue()
    test_get_priority_queue_empty()
    test_tree()
    test_huffman_encoding()
    test_huffman_decoding()
    test_huffman_decoding_repetitive_data()
    test_huffman_decoding_empty_data()

TEST_SUITE()