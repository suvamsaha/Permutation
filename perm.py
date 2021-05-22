def permutation(data):
    s = list()
    if 1 == len(data):
        return {data}
    for i in range(len(data)):
        s = s + list(map(lambda x: data[i] + x, permutation(data[:i]+data[i+1:])))
    return set(s)


print(permutation('abc'))

def permutation(data):
    s = list()
    if 1 == len(data):
        return data
    for i in range(len(data)):
        l = permutation(data[:i]+data[i+1:])
        for x in l:
            s.append(data[i] + x)
    return s


#print(permutation('abcd'))


def combination(data):
    s = list()
    if 1 == len(data):
        return [data]
    for i in range(len(data)):
        l = combination(data[:i]) + combination(data[i + 1:])
        for x in l:
            s.append(x)
            s.append(data[i] + x)
    return s

print(set(combination('ababccc')))
