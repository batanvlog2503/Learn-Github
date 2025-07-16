if __name__ == "__main__":
    a = [1, 2, 1, 3, 1, 4, 1, 0, 2, 5]
    d = {}

    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    for x, y in d.items():
        print(x, y)
    b = list(d.items())
    b.sort(key = lambda x : x[0])
    print(b)

    #dict comprehension

    d2 = {x : x ** 2 for x in a}

    print(d2)

    s = 'abc'
    d = {x : x * 3 for x in s}
    print(d)

