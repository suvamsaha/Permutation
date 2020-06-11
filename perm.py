def permutation(data):
    s = list()
    if 1 == len(data):
        return {data}
    for i in range(len(data)):
        s = s + list(map(lambda x: data[i] + x, permutation(data[:i]+data[i+1:])))
    return set(s)


print(permutation('abc'))
