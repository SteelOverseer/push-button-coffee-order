import os
from terminal_shop import Terminal
from dotenv import dotenv_values

config = dotenv_values(".env")

token = config["TERMINAL_BEARER_TOKEN"]
environment = config["ENVIRONMENT"]

print("Token: ", token)
print("environment: ", environment)

# client = Terminal(
#     bearer_token=os.environ.get("TERMINAL_BEARER_TOKEN"),  # This is the default and can be omitted
#     # defaults to "production".
#     environment="dev",
# )

# product = client.product.list()
# print(product.data)