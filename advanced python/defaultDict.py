from collections import defaultdict

dic = defaultdict(list)

with open("1.txt",'r') as f:
    data = f.readlines()
    for line in data:
        tmp = line.split(" ")
        dic[tmp[0]].append(int(tmp[1][:-1]))
print(dic['a'])

l = [12,132,12]
l.pop()