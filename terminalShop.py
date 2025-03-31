from terminal_shop import Terminal
from terminal_shop.types import AddressListResponse, ProductGetResponse, CardListResponse, Card, Address, Product, OrderCreateResponse, OrderCreateParams



def getClient(token: str):
  client = Terminal(
    bearer_token=token,  # This is the default and can be omitted
    environment="dev", # defaults to "production".
  )
  return client

def getProduct(client: Terminal, id: str):
  try:
    product : ProductGetResponse = client.product.get(id)
    return product.data
  except:
    print("Product ErrorError")

def getAddress(client: Terminal):
  try:
    addresses : AddressListResponse = client.address.list()

    if len(addresses.data) > 0:
      return addresses.data[0]
    else:
      print("Address not found")
  except:
    print("Address Error")

def getCard(client: Terminal):
  try:
    cards : CardListResponse = client.card.list()

    if len(cards.data) > 0:
      return cards.data[0]
    else:
      print("Card not found")
  except:
    print("Get card error")

def createOrder(client: Terminal, card: Card, address: Address, product: Product, quantity: int):
  print("creating order")
  try:
    resp : OrderCreateResponse = client.order.create(
      address_id = address.id, 
      card_id = card.id, 
      variants = { 
        product.variants[0].id: quantity
      }
    )
    print(f"response: {resp}")
    if resp.data:
      print(f"Order created id: {resp.data}")
    else:
      print("Error response")
  except Exception as e:
    print(f"Error creating order: {e}")