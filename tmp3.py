from dataclasses import dataclass


# クラス分け
# @dataclass
@dataclass(frozen=True)
class ProductData:
    name: str
    cost: int


class Product(ProductData):

    def __init__(self, name2, cost2):
        super().__init__()
        # self.name = "aaa"
        self.name2 = name2
        self.cost2 = cost2

    def price_confirmed(self, rate: float) -> int:
        price = int(round(self.cost * rate, 0))
        return price

    def renamer(self, new_name: str):
        self.name = new_name


ice = Product("アイス", 99)
ice_price = ice.price_confirmed(1.203)

print(ice)
print(f'{ice.name}:{ice_price}円')

# ice.renamer("バニラアイス")
# print(ice.name)

print({ice})
