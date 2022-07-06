class Car:
    wheels = 4
    is_engine = False
    make = None
    model = None  # None is similar to initialize 0

    def make_engine_on(self):
        self.is_engine = True

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return (f'My engine status is { "on" if self.is_engine else "Off"}' #if condition is used within { }
                f'and My bike model is {self.model}')  #to define string in single line use within ' '


bmw = Car("SClass", "2018")
print("Engine status--", bmw.is_engine)
bmw.make_engine_on()
print("Engine status after calling engine on method--", bmw.is_engine)
print(bmw.__repr__())
