import time
from dotenv import dotenv_values
from terminal_shop import Terminal
from terminal_shop.types import Product, Address, Card
from terminalShop import getClient, getProduct, getAddress, getCard, createOrder
from pynput import keyboard

config = dotenv_values(".env")

token = config["TERMINAL_BEARER_TOKEN"]
environment = config["ENVIRONMENT"]
darkModeID = config["DARK_MODE"]
orderQty : int = int(config["ORDER_QTY"])

client : Terminal = None
darkMode : Product = None
shipAddress : Address = None
card : Card = None

client = getClient(token)
darkMode = getProduct(client, darkModeID)
shipAddress = getAddress(client)
card = getCard(client)

def on_press(key):
  try:
    if key == keyboard.Key.enter:
      createOrder(client, card, shipAddress, darkMode, orderQty)
      time.sleep(5)
      return False  # Stop the listener
  except AttributeError:
      pass

def poll_enter():
  with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

while True:
  if(True): # Switch on
    poll_enter() # This flow will need to change for button press