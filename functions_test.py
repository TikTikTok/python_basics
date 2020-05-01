def getAverage(mylist) :
    value = sum(mylist)/len(mylist)
    return value

def getAverage1(mylist) :
    return None

print(getAverage([1,2,3,4,5,6]))
print(getAverage1([1,2,3,4,5,6]))
print(type(getAverage),type(sum))