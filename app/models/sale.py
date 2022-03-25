import faust
from decimal import Decimal

class Sale(faust.Record, coerce=True):
  amount: Decimal
  state_abbreviation: str

  WA_TAX = Decimal('0.065')

  # we'd need a table obvs but lets just play with WA now, the closest state to
  # me that has a sales tax
  def calculateTax(self):
    if ( self.state_abbreviation == 'WA' ):
      return self.amount * self.WA_TAX

