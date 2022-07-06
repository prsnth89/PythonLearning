from Barclays import Barclays
from ICICI import ICICI


class TestBank:
      barclays=Barclays("Barclays",3000)
      barclays.showBank()
      barclays.limitOfBank()
      barclays.showWithdrawlLimit()

      icici=ICICI("ICICI",444)
      icici.showBank()
      icici.limitOfBank()
      icici.showTieUp()
