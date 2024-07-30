import json
from dataclasses import dataclass

_DB = []

# d: dict = {
#     'title': "",
#     'descr': "",
#     'price': "",
#     'img': "",
#     'mass': "",
#     'adres': {
#         'x': "1",
#         'y': '2'
#     }
# }
# d.get("")

@dataclass
class Address:
    number: int
    city: str
    street: str

@dataclass
class Card():
    title: str
    descr: str
    price: float
    address: Address

    def to_json(self) -> str:
        return json.dumps(self.__dict__)

    def add_to_db(self):
        _DB.append(self)

card1 = Card(title="title1",
            descr="58488",
            price=4848.5,
            address=Address(
                number=14,
                city='Moscow',
                street='street1'
                )
            )

card2 = Card(title="title2",
            descr="234324",
            price=3838,
            address=Address(
                number=15,
                city='Moscow',
                street='street2'
                )
            )

card3 = Card(title="title1",
            descr="12321",
            price=1818,
            address=Address(
                number=16,
                city='Moscow',
                street='street3'
                )
            )


card1.add_to_db()
card2.add_to_db()
card3.add_to_db()

print(_DB)
