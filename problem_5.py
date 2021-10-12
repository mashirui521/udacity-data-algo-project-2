import hashlib
from datetime import datetime

class Block:
    def __init__(self, data, previous_hash = None):
        self.timestamp = datetime.utcnow()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def has_previous(self):
        return self.previous_hash is not None

    def __repr__(self):
        return  '----------------------------\nBlock\ntimestamp=' + str(self.timestamp) + '\ndata=' + self.data + \
                    '\nprevious_hash=' + str(self.previous_hash) + '\nhash=' + str(self.hash) + \
                '\n----------------------------'

class BlockChain:
    def __init__(self):
        self.tail = None
        self.num_blocks = 0
        self.blocks = list()

    def append(self, data):
        if type(data) is not str:
            print('!!!Invalid input data {}. The data must be a string!!!'.format(data))
            return

        self.tail = Block(data, self.tail.hash if self.tail is not None else None)
        self.num_blocks += 1
        self.blocks.append(self.tail)

    def is_empty(self):
        return self.num_blocks == 0

    def __len__(self):
        return self.num_blocks

    def __repr__(self):
        output_string = ''
        for block in self.blocks:
            if not block.has_previous():
                output_string += str(block)
            else:
                output_string += '\n->\n' + str(block)
        return output_string

###################################  TEST  ###############################################
def test_invalid_int_input():
    print('\n--------------------   TEST_INVALID_INT_INPUT   ------------------')

    block_chain = BlockChain()
    block_chain.append(1)                 # invalid input, pop up a error message

    print('--------------------   END: TEST_INVALID_INT_INPUT   ------------------\n')

def test_none_input():
    print('\n--------------------   TEST_INVALID_NONE_INPUT   ------------------')

    block_chain = BlockChain()
    block_chain.append(None)              # invalid input, pop up a error message

    print('--------------------   END: TEST_INVALID_NONE_INPUT   ------------------\n')

def test():
    print('\n--------------------   TEST   ------------------')

    block_chain = BlockChain()
    block_chain.append('1')
    block_chain.append('2')
    block_chain.append('3')

    print('\nBlock Chain:\n')
    print(block_chain)                    # output block chain with block data = 1, 2, 3, in order

    print('--------------------   END: TEST   ------------------\n')

def TEST_SUITE():
    test()
    test_invalid_int_input()
    test_none_input()

TEST_SUITE()