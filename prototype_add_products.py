import os
from dotenv import load_dotenv

from woocommerce import API


load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")

wcapi = API(
    url="https://4.kpipartners.ru",
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    timeout=50,
)

# pr = {
#     "name": "nothinafdfd",
#     #     # "type": "simple",
#     "regular_price": "5000",
#     #     # "stock_quantity": 10,
#     #     # "short_description": "just an example product",
#     #     # "description": "This is just an example product, created with the Woocommerce REST API",
#     #     # "categories": [{"id": 17}],
#     "images": [
#         {
#             "src": "https://images.wbstatic.net/c516x688/new/9510000/9512621-1.jpg",
#             "alt": "example-image",
#         }
#     ]
#     #     # "images": "https://linuxconfig.org/images/linuxconfig_logo.png",
# }


def add_to_wp(pr):
    wcapi = API(
        url="https://4.kpipartners.ru",
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        timeout=50,
    )
    response = wcapi.post("products", pr)


# add_to_wp(pr)

# print(response.json())
