def getRow(rowIndex):

    array = []

    for i in range(rowIndex + 1):
        
        array.append(nCk(rowIndex, i))
        
    return array

    
def nCk(n, k):

    import math
    
    return int(math.factorial(n) / (math.factorial(k) * (math.factorial(n - k))))
    

print(getRow(4))

