def selection(xs):
    steps = []
    for i in range(0,len(xs)):
        k = i
        for j in range(i+1, len(xs)):
            nextstep = []
            for x in xs:
                nextstep.append(x)
            
            steps.append(nextstep)
            if xs[j] < xs[k]:
                k = j
        swap(xs, i, k)
    return steps

def swap(xs, i , j):
    xs[i], xs[j] = xs[j], xs[i]
    return xs