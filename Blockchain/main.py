from Block import Block
from Blockchain import Blockchain
from time import time

blockchain = Blockchain()

new_block = Block(str(int(time())), ({"from": "Polina", "to": "Max", "amount": 203}),
                  blockchain.getLastBlock().getHash(), difficulty=blockchain.getDifficulty())
blockchain.addBlock(new_block)
print(blockchain)