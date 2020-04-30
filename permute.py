import random

def permute(k):
    ordered = k
    permutation = []
    for i in range(0,len(ordered)):
        choice = random.choice(ordered)
        ordered.remove(choice)
        permutation.append(choice)
    return permutation

print(permute(4))