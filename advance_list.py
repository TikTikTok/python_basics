def returnValue(lists):
    return [temp if isinstance(temp, int) else 0 for temp in lists]

def sums(lists):
    return sum([int(temp) for temp in lists])

def foo(lst):
    return sum([int(i) for i in lst])

print(returnValue([334,45,67,'334','hello']))
print(foo(['334','45','67','334','2322']))
print(sums(['334','45','67','334','2322']))