import faust

from .models.sale import Sale
from decimal import Decimal

SALES_TOPIC_NAME = 'streams-plaintext-input'
TAX_TOPIC_NAME = 'streams-wordcount-output'
APP_NAME = 'taxservice'
BROKER = 'kafka://localhost:9092'

app = faust.App(APP_NAME, broker=BROKER)
sales_topic = app.topic(SALES_TOPIC_NAME, value_type=Sale)
tax_topic = app.topic(TAX_TOPIC_NAME, value_type=Decimal)

@app.agent(sales_topic)
async def read_sale(sales):
  async for sale in sales:
    tax = sale.calculateTax()
    print(f'Sale for {str(sale.amount)}')
    print(f'Tax is {str(tax)}')
    await tax_topic.send(key="tax", value=tax)

if __name__ == '__main__':
    app.main()