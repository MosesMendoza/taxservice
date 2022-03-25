import faust
from decimal import Decimal

class Sale(faust.Record):
  amount: Decimal

