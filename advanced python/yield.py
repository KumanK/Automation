def generateNums(d):
    for i in range(1,d+1):
        yield i

O = generateNums(10)
# print(O.__next__())
# print(O.__next__())
# print(O.__next__())
# print(O.__next__())
# print(O.__next__())
# print(O.__next__())
# print(O.__next__())
# print(O.__next__())

def gen1(stri):
    for i in range(len(stri) - 1, -1, -1):
        yield stri[i]


s1 = gen1('2912')
print(s1.__next__())