from time import time
from Block import Block
import json


class Blockchain(object):
    def __init__(self):
        self.chain = [Block(str(int(time())))]
        self.difficulty = 1
        self.blockTime = 10000

    def __repr__(self):
        return json.dumps([{'data': item.data,
                            'timestamp': item.timestamp,
                            'nonce': item.nonce,
                            'hash': item.hash,
                            'prevHash': item.prevHash}
                           for item in self.chain], indent=4)

    def getDifficulty(self):
        return self.difficulty

    def getLastBlock(self):
        return self.chain[len(self.chain) - 1]

    def addBlock(self, block: Block):
        prevHash = (self.getLastBlock()).hash
        if not (block.prevHash == prevHash):
            return False
        self.chain.append(block)
        self.difficulty += (-1, 1)[int(time()) - int(self.getLastBlock().timestamp) < self.blockTime]

    def isValid(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            prevBlock = self.chain[i - 1]

            if currentBlock.hash != currentBlock.getHash() or prevBlock.hash != currentBlock.prevHash:
                return False

        return True

    def __repr__(self):
        return json.dumps([{'data': item.data, 'timestamp': item.timestamp, 'nonce': item.nonce, 'hash': item.hash,
                            'prevHash': item.prevHash} for item in self.chain], indent=4)
