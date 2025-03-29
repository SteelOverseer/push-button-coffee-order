import os
from dotenv import dotenv_values
from terminal_shop import Terminal
from terminal_shop.types import Order, OrderCreateResponse, OrderListResponse, OrderGetResponse
from terminal_shop.types import (
  Address,
  AddressCreateResponse,
  AddressListResponse,
  AddressDeleteResponse,
  AddressGetResponse,
)

config = dotenv_values(".env")

token = config["TERMINAL_BEARER_TOKEN"]
environment = config["ENVIRONMENT"]
darkModeID = config["DARK_MODE"]
darkMode = None
shipAddress = None

client = Terminal(
  bearer_token=token,  # This is the default and can be omitted
  environment="dev", # defaults to "production".
)

try:
  product = client.product.get(darkModeID)
  darkMode = product.data
except:
  print("Product ErrorError")

try:
  addresses = client.address.list()

  if len(addresses.data) > 0:
    shipAddress = addresses.data[0]
  else:
    print("Address not found")
except:
  print("Address Error")


print(darkMode)
print(shipAddress)

# create order needs addressid, card id, varients with qty