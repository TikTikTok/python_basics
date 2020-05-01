def getAverage(value) :
    if isinstance(value, dict):
        print('Dictionary')
        the_mean = sum(value.values())/len(value)
    elif isinstance(value, list):
        print('List')
        the_mean = sum(value)/len(value)
    else:
        the_mean = 5000
    return the_mean

print(getAverage([1,2,3,4,5,6]))
print(getAverage({'Chandan':100,'Neha':200,'Singh':5000}))
print(getAverage('Hello'))
print(type(getAverage),type(sum))