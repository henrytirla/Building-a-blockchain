import json
from datetime import datetime
from hashlib import sha256
import random
class Blockchain(object):
    def __init__(self):
        self.chain=[]
        self.pending_transactions=[]

        #Create the Genesis block

        print("Creating genesis block")
        self.new_block()
    @property
    def last_block(self):
        # Gets the latest block in the chain
        #Return the last block in the chain
        return self.chain[-1] if self.chain else None

    def new_block(self,previous_hash=None):
        #Generates a newblock and adds it to the chain
        block={
            'index': datetime.utcnow().isoformat(),
            'timestamp': self.pending_transactions,
            'transactions': self.pending_transactions,
            'previous_hash': self.last_block["hash"] if self.last_block else None,
            'nonce': format(random.getrandbits(64), "x"),
        }

        #Get Hash of new block and add it to this block
        block_hash= self.hash(block)
        block["hash"]=block_hash

        #Reset list of pending transactions
        self.pending_transactions=[]
        # #Add the block to the chain
        # self.chain.append(block)
        # print(f"Created block{block['index']}")
        return block


    @staticmethod
    def hash(block):
        #Ensure dictionary is sorted to avoid inconsistent hashes
        block_string= json.dumps(block,sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    def new_transaction(self,sender,recipient,amount):
        #Adds a new transaction to the list of pending transactions
        self.pending_transactions.append({
            "recipient":recipient,
             "sender": sender,
              "amount": amount,
        })

    @staticmethod
    def valid_block(block):
        #Checks if block's hash starts with 0000
        return block["hash"].startswith("0000")

    def proof_of_work(self):
        while True:
            new_block= self.new_block()
            if self.valid_block(new_block):
                break
        self.chain.append(new_block)
        print("Found a new Block:", new_block)

    def valid_hash(self):
        pass


