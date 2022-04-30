class happy:
    def __init__(self):
        print "I am happy"
    def _get_status(self):
        return "Happy"

class happified(happy):
    def __init__(self):
        print "I am happified"
    def get_status(self):
        return "Happified"

hp = happy()
print hp.get_status()
# hpd = happified()
# print hpd.get_status()