import sys

class Program():
    def __init__(self):
        self.name = "World"
    def Condition(self):
        if(len(sys.argv) > 1):
            self.name = sys.argv[1]
    def Print(self):
        print("Hello " + str(self.name) + "!")

prog = Program()
prog.Condition()
prog.Print()
