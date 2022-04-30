import csv

# with open('temp.csv') as fi:
#     csRead = csv.reader(fi,delimiter=',')
#     for line in csRead:
#         print line
with open('temp.csv') as fi:
    csRead = csv.DictReader(fi)
    for line in csRead:
        print line
