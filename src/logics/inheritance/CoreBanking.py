class CoreBanking:
    bankName = None
    limit = None

    def __init__(self, bankName, limit):
        self.bankName = bankName
        self.limit = limit

    def showBank(self):
        print(f'My bank name is {self.bankName}')

    def limitOfBank(self):
        print(f'My bank limit is {self.limit}')
