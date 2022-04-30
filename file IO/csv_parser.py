import csv

# with open('temp.csv') as fi:
#     csRead = csv.reader(fi,delimiter=',')
#     for line in csRead:
#         print line

def open_read(fileName):
    with open(fileName) as fi:
        csRead = csv.DictReader(fi)
        for line in csRead:
            print line

tags = ['status','fsType','whitelisted']

entries = [[1,'ext4','Yes'],
           [0,'ext3','Yes'],
           [1,'ext2','No']]
with open('sample.csv','w') as file:
    csvWriter = csv.writer(file)
    csvWriter.writerow(tags)
    for row in entries:
        csvWriter.writerow(row)
open_read('sample.csv')