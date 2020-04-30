def quickIter(xs, steps):
    if xs == []:
        return [], steps
    pivot = xs[0]
    less, same, more = [], [], []
    for x in xs:
        nextstep = []
        for y in xs:
            nextstep.append(y)
        
        steps.append(nextstep)
        print(less, same, more, xs)

        if x < pivot:
            less.append(x)
        elif x == pivot:
            same.append(x)
        else:
            more.append(x)
    return (quickIter(less, steps)[0] + same + quickIter(more, steps)[0]), steps

def quick(xs):
    steps = []
    return quickIter(xs, steps)[1]

print(quick([4,3,2,5,1]))
