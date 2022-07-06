from src.logics.inheritance.CoreBanking import CoreBanking


class Barclays(CoreBanking):

      def showWithdrawlLimit(self):
          limitOfWithrawl = 3000
          print(f'Withdrawl limit of {self.bankName} bank is {limitOfWithrawl}')
