import sys

def format_traceback(exc_type, exc_value, exc_traceback):
    print("Something wrongg ! ")
    print(exc_type)
    print(exc_value)
    print(list(exc_traceback))
    
sys.excepthook = format_traceback    
def adder():
    print(10+'hello')
    
adder()