import faust

from .models.sale import Sale

TOPIC = 'streams-plaintext-input'
APP_NAME = 'taxservice'
BROKER = 'kafka://localhost:9092'

app = faust.App(APP_NAME,
                broker=BROKER)

@app.agent(TOPIC, value_type=Sale)
async def read_sale(sales):
  async for sale in sales:
    print(f'Sale for {str(sale.amount)}')

if __name__ == '__main__':
    app.main()