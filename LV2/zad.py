from datetime import datetime
import hashlib

class Block:
    def __init__(self, name, str, amount):
        self.index = len(blockchainList)
        self.name=name
        self.prevHash = getprevHash()
        result = hashlib.sha256(str.encode())
        self.selfHash = result.hexdigest()
        self.timeOfCreation = datetime.now()
        self.wallet = Wallet(self.selfHash, amount)
        self.transactionList = []
    
class Transaction:
    def __init__(self, sender, amount, getter):
        self.sender = sender
        self.amount = amount
        self.getter = getter
        transactionFunc(sender, amount, getter)
        appendTransaction(blockchainList , self.sender, self.getter, self)

class Wallet:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

#functions

def appendTransaction(list, sender, getter, transaction):
    for block in list:
        if block.name == sender or block.name == getter:
            block.transactionList.append(transaction)


def transactionFunc(sender, amount, getter):
    for block in blockchainList:
        if sender == block.name:
            block.wallet.amount = block.wallet.amount - amount
        elif getter == block.name:
            block.wallet.amount = block.wallet.amount + amount

def getprevHash():
    prevIndex = len(blockchainList) - 1
    if ( prevIndex == -1 ):
        return "No previous block"
    else:
        prevHash = blockchainList[prevIndex].selfHash
        return prevHash

def printTransactions(self):  
    print("\n\t Transactions for", self.name)
    for x in self.transactionList:
        print("\nSender:",x.sender,"\tAmount:", x.amount,"\tReceiver:", x.getter, "\n")

#main

blockchainList = []

blockchainList.append(Block("UserOne", "RandomPassword" , 50))
blockchainList.append(Block("UserTwo", "RandomPassword2" , 50))

tact = Transaction("UserOne", 15, "UserTwo")

print("\nBlocks in blockchain and their transactions: \n")

for block in blockchainList:
    print("\tBlock index: ", block.index,
        "\n\tBlock name: ", block.name, 
        "\n\tHash of the previous block: ", block.prevHash, 
        "\n\tHash of this block: ", block.selfHash, 
        "\n\tTime of creation: ", block.timeOfCreation)
    
    printTransactions(block)




