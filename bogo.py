import duplicate
import random

def permute(xs):
    ordered = duplicate.dup(xs)
    permutation = []
    for i in range(0,len(ordered)):
        choice = random.choice(ordered)
        ordered.remove(choice)
        permutation.append(choice)
    return permutation

def sorted(xs):
    for i in range(0, len(xs)-1):
        if xs[i] > xs[i+1]:
            return False
    return True

def bogo(xs):
    steps = []
    while sorted(xs) == False:
        nextxs = permute(xs)
        xs = duplicate.dup(nextxs)

        nextstep = []
        for x in xs:
            nextstep.append(x)
            
        steps.append(nextstep)
    return steps


            