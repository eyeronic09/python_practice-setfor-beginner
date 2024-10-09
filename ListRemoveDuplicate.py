def removedup(a):
    for item in a:
        if item not in newList:
            newList.append(item)
    return newList
    
a = [1, 2, 9, 2, 5, 4, 4, 5, 1, 9, 8]
newList = []
print(removedup(a))