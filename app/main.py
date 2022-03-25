import faust

from .models.sale import Sale
from decimal import Decimal

TOPIC = 'streams-plaintext-input'
APP_NAME = 'taxservice'
BROKER = 'kafka://localhost:9092'

app = faust.App(APP_NAME,
                broker=BROKER)

@app.agent(TOPIC, key_type=str, value_type=Decimal)
async def read_sale(sales):
  async for sale in sales.items():
    saleObj = Sale(sale)
    print(f'Sale for {str(saleObj.amount)}')

if __name__ == '__main__':
    app.main()