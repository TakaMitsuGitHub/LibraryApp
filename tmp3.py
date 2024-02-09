from dataclasses import dataclass


# クラス分け
# @dataclass
@dataclass(frozen=True)
class ProductData:
    name: str
    cost: int

class Product(ProductData):

    def price_confirmed(self, rate: float) -> int:
        price = int(round(self.cost * rate, 0))
        return price


ice = Product("アイス", 99)
ice_price = ice.price_confirmed(1.203)

print(ice)
print(f'{ice.name}:{ice_price}円')
print({ice})
