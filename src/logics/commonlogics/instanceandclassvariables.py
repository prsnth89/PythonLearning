class Variables:
    constantNo = 100  # class variables

    def __init__(self, a, b):
        self.a = a;  # instance variables should always be called by self.variable name
        self.b = b;

    def __int__(self):
        pass

    def add(self):
        print("Add---", self.a + self.b)

    def addNos(self):
        print("Add nos---", self.a + self.b + Variables.constantNo)


obj = Variables(4, 4)
obj.add()  #calling instance variables 4,4 in add method

obj2 = Variables(2.5,2.6)
obj2.add()
obj2.addNos()
