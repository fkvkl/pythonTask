def merge(*args):
    newList = []
    for i in args:
        newList.extend(i)
    newList.sort()
    for i in newList:
        yield i
