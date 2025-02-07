class Node:
    def __init__(self, freq, left=None, right=None):
        self.freq = freq
        self.left = left
        self.right = right
        self.huff = ''


with open("problem14_6.txt") as file:
    totalSymbols = file.readline().strip()
    symbols = []
    for line in file:
        node = Node(int(line))
        symbols.append(node)

# O(n)
def huffman(symbols):
    firstQueue = symbols
    secondQueue = []
    
    while True:
        
        if len(firstQueue) + len(secondQueue) == 1:
            if len(firstQueue) == 1:
                return firstQueue[0]
            else:
                return secondQueue[0]
        
        firstMin = None
        secondMin = None
        
        firstCandidate = firstQueue[0].freq + firstQueue[1].freq if len(firstQueue) > 1 else float("inf")
        secondCandidate = firstQueue[0].freq + secondQueue[0].freq if len(firstQueue) >= 1 and len(secondQueue) >= 1 else float("inf")
        thirdCandidate = secondQueue[0].freq + secondQueue[1].freq if len(secondQueue) > 1 else float("inf")
        
        winner = min(firstCandidate, secondCandidate, thirdCandidate)
        
        if winner == firstCandidate:
            firstMin = firstQueue.pop(0)
            secondMin = firstQueue.pop(0)
        elif winner == secondCandidate:
            firstMin = firstQueue.pop(0)
            secondMin = secondQueue.pop(0)
        else:
            firstMin = secondQueue.pop(0)
            secondMin = secondQueue.pop(0)
            
        
        firstMin.huff = '0'
        secondMin.huff = '1'
        
        newSymbol = Node(firstMin.freq+secondMin.freq, firstMin, secondMin)
        
        secondQueue.append(newSymbol)
    

# O(n)
def binaryCode(tree):
    codes = []
    def traverse(tree, val=''):
        newVal = val + tree.huff
        if tree.left != None:
            traverse(tree.left, newVal)
            
        if tree.right != None:
            traverse(tree.right, newVal)
            
        if tree.left == None and tree.right == None:
            codes.append(newVal)

    traverse(tree)
    
    return codes

def freq(e):
    return e.freq

# O(nlog(n))
symbols.sort(key=freq)

tree = huffman(symbols)

codes = binaryCode(tree)

# O(n)
print("Min: " + str(len(min(codes, key=len))))
print("Max: " + str(len(max(codes, key=len))))
