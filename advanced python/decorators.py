
import time

def decorator(time):
    print(time)

def retry_validate(func):
    def inner(*args,**kwargs):
        print(*args,**kwargs)
        for i in range(15):
            print("trying for {} time".format(str(i)))
            if func(*args):
                return True
        return False
    return inner

# @decorator(time=20)
@retry_validate
def validate(name):
    time.sleep(1)
    with open("C:\\Users\\kkuman.CORPZONE\\PycharmProjects\\MACC_Automation\\venv\Scripts\\1.log",'r') as w:
        for line in w.readlines():
            if name in line:
                return True
    return False


def smart_division(func):
    def inner(a,b):
        if b == 0:
            print('Not possible')
            return
        else:
            return func(a,b)
    return inner

@smart_division
def division(a,b):
    return a/b
validate("xxx")
#
# division(9,0)
# print(division(9,3))










