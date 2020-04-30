def insertion(xs):
    steps = []
    n = len(xs)
    for j in range(0,n-1):
        key = xs[j+1]
        i = j
        while i >= 0 and xs[i] > key:
            nextstep = []
            for x in xs:
                nextstep.append(x)
            
            steps.append(nextstep)

            xs[i+1] = xs[i]
            xs[i] = key
            i = i - 1
        xs[i+1] = key
    steps.append(xs)
    return steps