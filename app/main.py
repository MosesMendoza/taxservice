import faust

from .models.sale import Sale
from decimal import Decimal

TOPIC = 'streams-plaintext-input'
APP_NAME = 'taxservice'
BROKER = 'kafka://localhost:9092'

app = faust.App(APP_NAME,
                broker=BROKER)

@app.agent(TOPIC, value_type=Sale)
async def read_sale(sales):
  async for sale in sales:
    tax = sale.calculateTax()
    print(f'Sale for {str(sale.amount)}')
    print(f'Tax is {str(tax)}')

if __name__ == '__main__':
    app.main()