from dataclasses import dataclass


# 通常
# @dataclass
@dataclass(frozen=True)
class Product:
    name: str
    cost: int

    def price_confirmed(self, rate: float) -> int:
        price = int(round(self.cost * rate, 0))
        return price


ice = Product("アイス", 99)
ice_price = ice.price_confirmed(1.203)

print(ice)
print(f'{ice.name}:{ice_price}円')
print({ice})
