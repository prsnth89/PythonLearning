from logics.return_val import IWeb


class tes1(IWeb):

    def find(self):
        print("find")
        return self

    def clear(self):
        print("clear")
        return self