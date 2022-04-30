import sys

def hack_print(argument):
    orig_stdout = sys.stdout
    with open("App.log",'a') as f:
        sys.stdout=f
        print(argument)
        sys.stdout=orig_stdout
