
def nested_sum(t):
    nestedSum = 0
    for i in range(len(t)):
        nestedSum += sum(t[i])
    return nestedSum

def cumsum(t):
    cumList = []
    for i in range(len(t)):
        cumList.append(sum(t[0:i]))
    return cumList

def middle(t):
    return t[1:len(t) - 1]

def chop(t):
    del t[0]
    del t[-1]

def is_sort(t):
    sortList = t[:]
    sortList.sort()
    if sortList == t:
        return True
    else:
        return False