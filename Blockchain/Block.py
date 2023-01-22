from hashlib import sha256
from time import time

class Block:
    def __init__(self, timestamp=None, data=None, prevBlockHash = None, difficulty = 1):
        self.timestamp = timestamp or time()
        self.data = [] if data is None else data
        self.nonce = 0
        self.prevHash = prevBlockHash
        self.hash = self.getHash()
        self.mine(difficulty)

    def getHash(self):
        hash = sha256()
        hash.update(str(self.prevHash).encode('utf-8'))
        hash.update(str(self.timestamp).encode('utf-8'))
        hash.update(str(self.data).encode('utf-8'))
        hash.update(str(self.nonce).encode('utf-8'))
        return hash.hexdigest()

    def mine(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.getHash()