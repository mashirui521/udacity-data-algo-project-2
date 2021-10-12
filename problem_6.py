import hashlib

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def is_equal(self, value):
        return self.value == value

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while not node.is_equal(value):
            if node.next:
                node = node.next
            else:
                node.next = Node(value)
                break

    def find(self, value):
        if value is None:
            return False
        node = self.head
        while node:
            if node.is_equal(value):
                return True
            node = node.next
        return False

    def __repr__(self):
        output_string = ''
        if self.head is None:
            output_string += 'empty'
        else:
            node = self.head
            while node:
                output_string += str(node) + ' '
                node = node.next
        return output_string

def union(llist_1, llist_2):
    node = llist_2.head
    while node is not None:
        llist_1.append(node.value)
        node = node.next
    return llist_1

def intersection(llist_1, llist_2):
    llist_intersection = LinkedList()
    node = llist_1.head
    while node:
        if llist_2.find(node.value):
            llist_intersection.append(node.value)
        node = node.next
    return llist_intersection

###################################  TEST  ###############################################
def test_no_intersection():
    print('\n--------------------   TEST_NO_INTERSECTION   ------------------')

    llist_1 = LinkedList()
    llist_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]
    
    for item_1, item_2 in zip(element_1, element_2):
        llist_1.append(item_1)
        llist_2.append(item_2)

    print('LinkedList 1: {}'.format(llist_1))                         # output: 3 2 4 35 6 65
    print('LinkedList 2: {}'.format(llist_2))                         # output: 1 7 8 9 11 21

    llist_intersection = intersection(llist_1, llist_2)
    print('LinkedList Intersection: {}'.format(llist_intersection))   # output: empty

    print('\n--------------------   TEST_NO_INTERSECTION   ------------------')

def test_intersection():
    print('\n--------------------   TEST_INTERSECTION   ------------------')

    llist_1 = LinkedList()
    llist_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]
    
    for item_1, item_2 in zip(element_1, element_2):
        llist_1.append(item_1)
        llist_2.append(item_2)

    print('LinkedList 1: {}'.format(llist_1))                         # output: 3 2 4 35 6 65
    print('LinkedList 2: {}'.format(llist_2))                         # output: 1 7 8 9 11 21

    llist_intersection = intersection(llist_1, llist_2)
    print('LinkedList Intersection: {}'.format(llist_intersection))   # output: empty

    print('\n--------------------   TEST_INTERSECTION   ------------------')

def test_union():
    print('\n--------------------   TEST_UNION   ------------------')

    llist_1 = LinkedList()
    llist_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for item_1, item_2 in zip(element_1, element_2):
        llist_1.append(item_1)
        llist_2.append(item_2)

    print('LinkedList 1: {}'.format(llist_1))           # output: 3 2 4 35 6 65
    print('LinkedList 2: {}'.format(llist_2))           # output: 6 32 4 9 1 11 21

    llist_union = union(llist_1, llist_2)
    print('LinkedList Union: {}'.format(llist_union))   # output: 3 2 4 35 6 65 32 9 1 11 21

    print('--------------------   END: TEST_UNION   ------------------\n')

def test_find_value():
    print('\n--------------------   TEST_FIND_VALUE   ------------------')
    data = [3,2,4,35,6,65,6,4,3,21]
    llist = LinkedList()
    for item in data:
        llist.append(item)

    if llist.find(65):
        print('Pass')
    else: 
        print('Failed')

    if not llist.find(None):
        print('Pass')
    else: 
        print('Failed')
    print('--------------------   END: TEST_FIND_VALUE   ------------------\n')

def test_llist():
    print('\n--------------------   TEST_LLIST   ------------------')

    data = [3,2,4,35,6,65,6,4,3,21]
    llist = LinkedList()
    for item in data:
        llist.append(item)
    print('LinkedList: {}'.format(llist))               # output: 3 2 4 35 6 65 21

    print('--------------------   END: TEST_LLIST   ------------------\n')

def test_empty_list():
    print('\n--------------------   TEST_EMPTY_LIST   ------------------')

    data = []
    llist = LinkedList()
    for item in data:
        llist.append(item)
    print('LinkedList: {}'.format(llist))               # output: empty
    print('--------------------   END: TEST_EMPTY_LIST   ------------------\n')

def TEST_SUITE():
    test_llist()
    test_empty_list()
    test_find_value()
    test_union()
    test_intersection()

TEST_SUITE()