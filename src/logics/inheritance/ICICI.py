
from CoreBanking import CoreBanking


class ICICI(CoreBanking):
      tieUpWithBarclays=True
      tieUpWithHDFC=False
      def showTieUp(self):
          if self.tieUpWithBarclays:
              print(f'ICICI have tieup with Barclays')
          elif self.tieUpWithHDFC:
              print(f'ICICI bank have tieup with HDFC bank')
          else:
              print(f'ICICI doesnt have any tie up with any bank')