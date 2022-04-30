import sqlite3
import random


class dbInterface:
    def __init__(self,name):
        self.connection=sqlite3.connect("solidified.db")
        self.ccCursor = self.connection.cursor()
    def spawanTable(self):
        self.ccCursor.execute("""CREATE TABLE solidicoreFiles(
                filename text,
                rootdir text,
                inode integer
                )""")
    def fillDummyData(self):
        extensionChoices = [".sh",".py",".txt",".xml",".bin"]
        dirChoice = ['root','var','tmp']
        for num in range(1000):
            extchoice = random.choice(extensionChoices)
            rootdir = random.choice(dirChoice)
            fileName = 'file'+str(num)+extchoice
            inode = num
            # print choice
            self.ccCursor.execute("INSERT INTO solidicoreFiles VALUES ('{}','{}',{})".format(fileName,rootdir,inode))

    def execute(self,query):
        return self.ccCursor.execute(query)
